from django.urls import path

from reserve import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_restaurant, name='search_results'),
]
