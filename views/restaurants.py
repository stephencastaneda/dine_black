from django.http import HttpResponseServerError
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from dineblackapp.models import Restaurant

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Restaurant
        url = serializers.HyperlinkedIdentityField(
            view_name='restaurant',
            lookup_field='id'
        )
        fields = ('id', 'name', 'city', 'state', 'address', 'zip_code', 'phone_number', 'latitude', 'longitude')
        depth = 2

class Restaurants(ViewSet):

    def retrieve(self, request, pk=None):
        try:
            restaurant = Restaurant.objects.get(pk=pk)
            serializer = RestaurantSerializer(
                restaurant, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
            )
    
    def list(self, request):
        restaurants = Restaurant.object.all()
        serializer = RestaurantSerializer(
            restaurants,
            many=True,
            context={'request': request}      
        )
        return Response(serializer.data)