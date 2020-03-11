from django.urls import path
from . import views
from rest_framework_swagger.views import get_swagger_view


urlpatterns = [
    path('docs/', get_swagger_view(title='API Docs')),
    path('dish/', views.dish_list),
    path('dish/<int:dish_id>/', views.dish_detail),
]