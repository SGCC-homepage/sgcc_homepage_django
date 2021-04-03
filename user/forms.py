from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *


# abstractuser의 username을 학번으로 사용
class CreateAccount(UserCreationForm):
    password1 = forms.CharField(widget=forms.TextInput(attrs={'type': 'password', 'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'type': 'password', 'class': 'form-control'}))

    class Meta:
        model = User

        fields = ['name', 'username', 'major', 'phone', 'state', 'email', 'password1', 'password2']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '실명으로 입력해주세요'}),
            'username': forms.TextInput(attrs={'class': 'form-control',  'placeholder': '8자리 모두 입력해주세요(예시: 20210001)', 'pattern': '[0-9]{8}'}),
            'major': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'type': 'tel', 'pattern': "[0-9]{3}[0-9]{4}[0-9]{4}", 'class': 'form-control', 'placeholder': '- 없이 입력해주세요 (예시: 01012345678)'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
        }

        def clean(self):
            cleaned_data = super().clean()



class EditMyPage(forms.ModelForm):
    class Meta:
        model = User

        fields = ['email', 'phone', 'state']

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'text-end'}),
            'phone': forms.TextInput(
                attrs={'type': 'tel', 'pattern': "[0-9]{3}[0-9]{4}[0-9]{4}", 'class': 'text-end'}),
        }