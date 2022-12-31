from .models import car
from django import forms
class carForms(forms.ModelForm):
    class Meta:
        model=car
        fields='__all__'