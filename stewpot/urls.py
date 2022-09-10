from django.urls import path
from . import views as stewpot_views

urlpatterns = [
    path('share/<str:meal_id>', stewpot_views.share_recipe.as_view(), name='share-meal'),

    ]
