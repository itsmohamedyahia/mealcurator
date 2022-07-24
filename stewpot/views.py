from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView

# Within App Imports
from meals.models import mstr_recipe
from stewpot.models import share_meal

# Create your views here.

@login_required
class share_recipe(CreateView):
    login_required = True
    model = share_meal
    fields = ['title', 'text']
    success_url = reverse('share-meal', share_meal=self.object.id)

    # TODO: FIGURE OUT FORM VALIDATION, pass object id to shared_meal url when success

    def form_valid(self, form):
        shared_meal = form.save(commit=False)
        shared_meal.creator = User.objects.get(id=self.request.user.id)
        shared_meal.meal = mstr_recipe.objects.get(meal_id=meal_id)
        shared_meal.save()

    
    success_url = reverse('share-meal', shared_meal.id)    

def shared_meal(request, share_id):
    shared_meal = share_meal.objects.get(id=share_id)
    sender = request.User == shared_meal.creator

    context = {'shared': shared_meal,
               'shared_view': True,
               'sender_view': sender,
               'meals': shared_meal.meal}
    return render(request, 'stewpot/shared.html', context)






