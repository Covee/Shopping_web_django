from django.shortcuts import render
from .models import Dish
from rest_framework.decorators import api_view


@api_view(['GET'])
def dish_list(request):
    dishes = Dish.objects.all()
    
    #serializer