from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *


# abstractuser의 username을 email로 사용
class CreateAccount(UserCreationForm):
    password1 = forms.CharField(widget=forms.TextInput(attrs={'type': 'password', 'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'type': 'password', 'class': 'form-control'}))

    class Meta:
        model = User

        fields = ['name', 'student_id', 'major', 'username', 'phone', 'state']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'student_id': forms.TextInput(attrs={'class': 'form-control'}),
            'major': forms.Select(attrs={'class': 'form-control'}),
            'username': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'type': 'tel', 'pattern': "[0-9]{3}[0-9]{4}[0-9]{4}", 'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
        }


class CreateAccountTest(UserCreationForm):
    class Meta:
        model = User

        fields = '__all__'


class LogIn(forms.ModelForm):
    class Meta:
        model = User

        fields = ['email', 'password']

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'})
        }