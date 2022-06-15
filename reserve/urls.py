from inspect import getmembers, isabstract, isclass

from django.urls import path, include

from reserve.views import IndexView, RestaurantListView, RestaurantCreateView, RestaurantDetailView
from rest_framework import routers

from . import api
from .apifactory import ApiFactory


router = routers.DefaultRouter()
factory = ApiFactory()
for name, _type in getmembers(api, lambda c: isclass(c) and not isabstract(c)):
    model = factory.return_class(name)
    display_name = name.lower()[:len(name)-len('ViewSet')]
    router.register(display_name, model)


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('search/', RestaurantListView.as_view(), name='search_results'),
    path('restaurant/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant_detail'),
    path('create_restaurant/', RestaurantCreateView.as_view(), name='create_restaurant'),
]
