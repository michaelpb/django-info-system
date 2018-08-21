from django import forms
from .models import Person

class InfoBaseForm(forms.ModelForm):

class CreatePersonForm(InfoBaseForm):
    name = 'Person'
    class Meta:
        fields = (
            'name',
            'account',
            'email',
        )
        model = Person

class EditPersonForm(CreatePersonForm):
    pass

