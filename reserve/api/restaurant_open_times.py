from rest_framework import serializers, viewsets
from reserve.models import RestaurantOpenTime


class RestaurantOpenTimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RestaurantOpenTime
        fields = ['url', 'restaurant', 'weekday', 'open_time', 'close_time']


class RestaurantOpenTimeViewSet(viewsets.ModelViewSet):
    queryset = RestaurantOpenTime.objects.all()
    serializer_class = RestaurantOpenTimeSerializer
