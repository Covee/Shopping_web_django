from django.shortcuts import render, get_object_or_404
from .models import Dish, DishReview
from rest_framework.decorators import api_view
from .serializers import DishSerializer, DishReviewSerializer
from rest_framework.response import Response


@api_view(['GET'])
def dish_list(request):
    dishes = Dish.objects.all()
    
    serializer = DishSerializer(dishes, many=True)
    return Response(serializer.data)
    

# @api_view(['GET'])
# def dish_detail(request, dish_id);
# 	dish = get_object_or_404(Dish, id=dish_id)
#     serializer = DishSerializer(dish)
#     return Response(serializer.data)

@api_view(['GET'])
def dish_review_list(request):
    dish_reviews = DishReview.objects.all()
    
    serializer = DishReviewSerializer(dish_reviews, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def dish_review_detail(Request, dish_review_id):
    dish_review = get_object_or_404(DishReview, id=dish_review_id)
    serializer = DishReviewDetailSerializer(dish_review)
    return Response(serializer.data)


@api_view(['POST'])
def review_create(request, dish_id):
    serializer = DishReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(dish_id=dish_id)
        return Response(serializer.data)