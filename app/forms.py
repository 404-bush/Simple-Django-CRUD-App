from django import forms
from .models import crud

class CrudForms(forms.ModelForm):
    class Meta:
        model = crud
        fields = ("name" ,"age","email","branch","phone")

