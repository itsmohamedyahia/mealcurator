from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.models import User

# Within App Imports
from meals.models import mstr_recipe
from stewpot.models import share_meal

# Create your views here.


@login_required
def share_recipe(request, meal_id, title=None, message=None):

    if not title:
        title = 'A shared recipe from MealCurator.com'
    if not message:
        message = 'I thought you might like this recipe I found on MealCurator.com'
    shared_meal = share_meal.objects.create(
                    title=title,
                    creator=request.User,
                    text=message,
                    meal=mstr_recipe.objects.get(meal_id=meal_id)
                    )

    return redirect('share-meal', shared_meal=shared_meal.id)


def shared_meal(request, share_id):
    context = {'shared': share_meal.objects.get(id=share_id)}
    return render(request, 'stewpot/shared.html', context)






