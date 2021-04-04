from django import forms
from .models import *

class PersonDetailsForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'age', 'email', 'zipcode', 'profile_image']

class PersonForm(forms.Form):
    pass
