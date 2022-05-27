from email.headerregistry import Address
from django.db import models

# Create your models here.

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
