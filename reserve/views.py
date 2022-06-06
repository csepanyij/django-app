from typing import Any, Dict, List, Optional, Type

from django.conf import settings
from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.generic import View, ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.forms import Form
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.db.models import Model
from django.db.models.query import QuerySet

from .forms import SearchRestaurantForm, CreateRestaurantForm
from .models import Restaurant


class GenericReservationView(View):
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['media_url'] = settings.MEDIA_URL
        return context


class IndexView(GenericReservationView):
    form_class: Type[Model] = SearchRestaurantForm
    template_name: str = 'reserve/search_restaurant.html'

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = self.form_class()
        return render(request, self.template_name, {'form': form})


class RestaurantListView(GenericReservationView, ListView):
    model: Type[Model] = Restaurant
    context_object_name: str = 'restaurants'

    def get_queryset(self) -> QuerySet:
        self.form: SearchRestaurantForm = SearchRestaurantForm(data=self.request.GET or None)
        form = self.form
        if self.request.GET and form.is_valid():
            queryset: QuerySet = Restaurant.objects.filter(name__icontains=form.cleaned_data['name'])
        else:
            queryset: QuerySet = super().get_queryset()
        return queryset

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        context['form'] = self.form
        context['search_term'] = self.form.cleaned_data['name']
        return context


class RestaurantCreateView(GenericReservationView, LoginRequiredMixin, CreateView):
    template_name: str = 'reserve/create_restaurant.html'
    model: Type[Model] = Restaurant
    fields: List[str] = ['name', 'address', 'rating', 'description', 'image']

    def form_valid(self, form: Form) -> HttpResponse:
        form.instance.owned_by = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Restaurant has been created!')
        return reverse('index')


class RestaurantDetailView(GenericReservationView, DetailView):
    model: Type[Model] = Restaurant
    context_object_name: Optional[str] = 'restaurant'

    def get_queryset(self) -> QuerySet:
        print(self.kwargs['pk'])
        return Restaurant.objects.filter(pk=self.kwargs['pk'])

