from django.shortcuts import render
from .products import products
from rest_framework.decorators import api_view #restframework function based views
from rest_framework.response import Response #for returning data from the DB and showing it to the api
from .models import *
from .serializers import ProductSerializer

# Create your views here.

@api_view(['GET', 'POST']) #this is called an decorator
def getRoutes(request):
    return Response

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all() # Retruns all the products from the database
    serializer = ProductSerializer(products, many=True) # many=True we are returning multiple data, which is why its true
    return Response (serializer.data) # serializer.data = this gives the query set

@api_view(['GET']) # for viewing single product in a page
def getSingleProduct(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)

    return Response (serializer.data) # to return a _id product i need to pass the variable product that hold the _id value