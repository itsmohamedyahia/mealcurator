from django import forms
from .models import share_meal


class create_share_form(forms.ModelForm):
     def __init__(self, *args, **kwargs):
        self.meal_id = kwargs.pop('meal_id')
        self.creator = kwargs.pop('user')
        super(create_share_form, self).__init__(*args, **kwargs)
    
    class Meta:
        model = share_meal
        fields = [title, text]
