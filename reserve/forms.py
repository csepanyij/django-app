from dataclasses import fields
from django import forms
from django.forms import ModelForm
from reserve.models import Restaurant


class CreateRestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'


class SearchRestaurantForm(forms.Form):
    name = forms.CharField(label='Restaurant name', max_length=512)
