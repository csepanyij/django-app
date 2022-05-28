from django.urls import path

from reserve import views
from reserve.views import IndexView, RestaurantListView, RestaurantCreateView, RestaurantDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('search/', RestaurantListView.as_view(), name='search_results'),
    path('restaurant/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant_detail'),
    path('create_restaurant/', RestaurantCreateView.as_view(), name='create_restaurant'),
]
