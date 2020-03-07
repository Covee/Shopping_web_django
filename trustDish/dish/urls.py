from django.urls import path
from . import views

urlpatterns = [
    path('dish/', views.dish_list),
]