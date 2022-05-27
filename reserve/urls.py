from django.urls import path

from reserve import views

urlpatterns = [
    path('', views.index, name='index')
]
