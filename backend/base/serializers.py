from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class ProductSerializer(serializers.ModelSerializer): # This class turns the DB data in json format to sent it to the frontend api
    class Meta:
        model = Product
        fields = '__all__'