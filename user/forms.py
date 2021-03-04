from django import forms
from .models import *


class CreateAccount(forms.ModelForm):
    class Meta:
        model = User

        fields = ['name', 'student_id', 'major', 'email', 'phone', 'state', 'password']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'student_id': forms.TextInput(attrs={'class': 'form-control'}),
            'major': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'type': 'tel', 'pattern': "[0-9]{3}[0-9]{4}[0-9]{4}", 'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'})
        }


class LogIn(forms.ModelForm):
    class Meta:
        model = User

        fields = ['email', 'password']

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'})
        }