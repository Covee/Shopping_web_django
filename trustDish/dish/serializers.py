from rest_framework import serializers
from .models import Dish, DishReview

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['id', 'name', 'price', 'portion', 'thumbnail', 'image', 'description']


class DishReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishReview
        fields = ['id', 'dish',  'title', 'image', 'star']


class DishReviewDetailSerializer(serializers.ModelSerializer):
    dish_set = DishSerializer(many=True)
    class Meta:
        model = DishReview
        fields = ['id', 'title', 'image', 'star', 'dish_set',]

        