from .models import *
from django import forms


class Subjectsform(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ["name"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject Name'}),
        }
