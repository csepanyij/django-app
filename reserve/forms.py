from dataclasses import fields
from django import forms
from django.forms import ModelForm

# from betterforms.multiform import MultiModelForm

from reserve.models import Restaurant, RestaurantOpenTime


class SearchRestaurantForm(forms.Form):
    name = forms.CharField(label='Restaurant name', max_length=512, required=False)


class CreateRestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'


class CreateRestaurantOpenTimeForm(ModelForm):
    class Meta:
        model = RestaurantOpenTime
        fields = '__all__'


# class CreateRestaurantMultiForm(MultiModelForm):
#     pass