from django.urls import path
from . import views

urlpatterns = [
    path('dish/', views.dish_list),
    path('dish/<int:dish_id>/', views.dish_detail),
]