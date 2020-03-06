from django.contrib import admin
from .models import Dish, DishReview, DishQA

admin.site.register(Dish)
admin.site.register(DishReview)
admin.site.register(DishQA)