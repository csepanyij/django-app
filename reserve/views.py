from typing import Any, Dict, Optional, Type

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

from .forms import SearchRestaurantForm, CreateRestaurantForm
from .models import Restaurant


class GenericReservationView(View):
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['media_url'] = settings.MEDIA_URL
        return context


class IndexView(GenericReservationView):
    form_class = SearchRestaurantForm
    template_name = 'reserve/search_restaurant.html'

    def get(self, request: HttpRequest, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})


class RestaurantListView(GenericReservationView, ListView):
    model = Restaurant
    context_object_name = 'restaurants'

    def get_queryset(self):
        self.form = SearchRestaurantForm(data=self.request.GET or None)
        form = self.form
        if self.request.GET and form.is_valid():
            queryset = Restaurant.objects.filter(name__icontains=form.cleaned_data['name'])
        else:
            queryset = super().get_queryset()
        return queryset

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        context['search_term'] = self.form.cleaned_data['name']
        return context


class RestaurantCreateView(GenericReservationView, LoginRequiredMixin, CreateView):
    template_name: str = 'reserve/create_restaurant.html'
    model = Restaurant
    fields = ['name', 'address', 'rating', 'description', 'image']

    def form_valid(self, form: Form) -> HttpResponse:
        form.instance.owned_by = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Restaurant has been created!')
        return reverse('index')


class RestaurantDetailView(GenericReservationView, DetailView):
    model: Type[Model] = Restaurant
    context_object_name: Optional[str] = 'restaurant'

    def get_queryset(self):
        print(self.kwargs['pk'])
        messages.add_message(self.request, messages.INFO, 'Test message.')
        return Restaurant.objects.filter(pk=self.kwargs['pk'])

