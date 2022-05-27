from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect

from .forms import SearchRestaurantForm
from .models import Restaurant

# Create your views here.

def index(request):
    form = SearchRestaurantForm()
    context = {
        'form': form,
    }
    return render(request, 'reserve/search_restaurant.html', context)


def search_restaurant(request):
    if request.method == 'POST':
        form = SearchRestaurantForm(request.POST)
        if form.is_valid():
            restaurant_name = form.cleaned_data['name']
            restaurants = Restaurant.objects.filter(name__contains=restaurant_name)
            context = {
                'restaurants': restaurants,
            }
            return render(request, 'reserve/search_restaurant_results.html', { 'restaurants': restaurants })
    else:
        return HttpResponseRedirect(redirect_to='reserve.index')
