from django import forms
from .models import *

class PersonDetailsForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ['avatar', 'first_name', 'last_name', 'age', 'email', 'zipcode']

class PersonForm(forms.Form):
    pass
