from django.conf import settings
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.http.request import HttpRequest

from .forms import SearchRestaurantForm, CreateRestaurantForm
from .models import Restaurant


def index(request: HttpRequest):
    form = SearchRestaurantForm()
    context = {
        'form': form,
    }
    return render(request, 'reserve/search_restaurant.html', context)


def search_restaurant(request: HttpRequest):
    if request.method == 'POST':
        form = SearchRestaurantForm(request.POST)
        if form.is_valid():
            restaurant_name = form.cleaned_data['name']
            restaurants = Restaurant.objects.filter(name__icontains=restaurant_name)
            context = {
                'restaurants': restaurants,
                'search_term': restaurant_name,
                'media_url': settings.MEDIA_URL,
            }
            return render(request, 'reserve/search_restaurant_results.html', context)
    else:
        return HttpResponseRedirect(redirect_to='reserve.index')


def create_restaurant(request: HttpRequest):
    if request.method == 'POST':
        form = CreateRestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'reserve/create_restaurant.html', {'form': form, 'img_obj': img_obj})

    else:
        form = CreateRestaurantForm()
    return render(request, 'reserve/create_restaurant.html', {'form': form})
