from django.shortcuts import render, get_object_or_404
from .models import Dish
from rest_framework.decorators import api_view
from .serializers import DishSerializer
from rest_framework.response import Response



@api_view(['GET'])
def dish_list(request):
    dishes = Dish.objects.all()
    
    serializer = DishSerializer(dishes, many=True)
    return Response(serializer.data)
    

@api_view(['GET'])
def dish_detail(request, dish_id);
	dish = get_object_or_404(Dish, id=dish_id)
    serializer = DishSerializer(dish)
    return response(serializer.data)