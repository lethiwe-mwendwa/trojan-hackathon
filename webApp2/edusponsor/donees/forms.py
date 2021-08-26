from django import forms
from . import models

class CreateDonee(forms.ModelForm):
    class Meta:
        model = models.donee
        fields = ['name', 'slug', 'message', 'email', 'contact', 'thumb',]
