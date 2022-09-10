from venv import create
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import create_share_form

# Within App Imports
from meals.models import mstr_recipe
from stewpot.models import share_meal

# Create your views here.

'''
class share_recipe(CreateView):
    login_required = True
    form_class = share_meal

    #success_url = reverse('share-meal', share_meal=self.object.id)

    # TODO: FIGURE OUT FORM VALIDATION, pass object id to shared_meal url when success


    def form_valid(self, form):
        shared_meal = form.save(commit=False)
        shared_meal.creator = User.objects.get(id=self.request.user.id)
        
        shared_meal.save()
        return redirect('welcome')
        
    def get_form_kwargs(self, *args, **kwargs):
        form_kwargs = super(share_recipe, self).get_form_kwargs(*args, **kwargs)
        form_kwargs['meal'] = self.request.meal_id
        form_kwargs['user'] = self.request.user
        
        return form_kwargs
    
   # success_url = reverse('share-meal', shared_meal.id)    
'''
def share_recipe(request, meal_id):
    form = create_share_form()
    if request

def shared_meal(request, share_id):
    shared_meal = share_meal.objects.get(id=share_id)
    sender = request.User == shared_meal.creator

    context = {'shared': shared_meal,
               'shared_view': True,
               'sender_view': sender,
               'meals': shared_meal.meal}
    return render(request, 'stewpot/shared.html', context)






