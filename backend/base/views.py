from django.shortcuts import render
from .products import products
from rest_framework.decorators import api_view #restframework function based views
from rest_framework.response import Response #for returning data from the DB and showing it to the api

# Create your views here.

@api_view(['GET', 'POST']) #this is called an decorator
def getRoutes(request):
    return Response

@api_view(['GET'])
def getProducts(request):
    return Response (products)

@api_view(['GET']) # for viewing single product in a page
def getSingleProduct(request, pk):
    product = None
    for i in products:
        if i["_id"] == pk:
            product = i
            break

    return Response (product) # to return a _id product i need to pass the variable product that hold the _id value