from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
    class Rating(models.IntegerChoices):
        VERY_BAD = 1
        BAD = 2
        NEUTRAL = 3
        GOOD = 4
        VERY_GOOD = 5

    name = models.CharField(max_length=512, blank=False)
    address = models.CharField(max_length=512, blank=False)
    rating = models.IntegerField(default=Rating.NEUTRAL, choices=Rating.choices)
    description = models.CharField(max_length=512, blank=True)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    owned_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


class RestaurantOpenTime(models.Model):
    class Weekdays(models.IntegerChoices):
        MONDAY = 0
        TUESDAY = 1
        WEDNESDAY = 2
        THURSDAY = 3
        FRIDAY = 4
        SATURDAY = 5
        SUNDAY = 6

    restaurant = models.ForeignKey(to=Restaurant, on_delete=models.CASCADE)
    weekday = models.IntegerField(choices=Weekdays.choices)
    open_time = models.TimeField()
    close_time = models.TimeField()
