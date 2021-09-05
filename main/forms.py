from django import forms
from django.contrib.auth.forms import UserCreationForm

from api.user.models import User


# abstractuser의 username을 학번으로 사용
class CreateAccount(forms.ModelForm):
    reason = forms.CharField(widget=forms.Textarea(attrs={'class': 'w-100'}), required=True)
    read_notice = forms.BooleanField(widget=forms.CheckboxInput(attrs={'type': 'checkbox', 'class': 'form-check-input'}), required=True)

    class Meta:
        model = User

        fields = ['name', 'username', 'major', 'second_major', 'third_major', 'phone', 'email']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '실명으로 입력해주세요'}),
            'username': forms.TextInput(attrs={'class': 'form-control',  'placeholder': '8자리 모두 입력해주세요(예시: 20210001)', 'pattern': '[0-9]{8}'}),
            'major': forms.Select(attrs={'class': 'form-control'}),
            'second_major': forms.Select(attrs={'class': 'form-control'}),
            'third_major': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'type': 'tel', 'pattern': "[0-9]{3}[0-9]{4}[0-9]{4}", 'class': 'form-control', 'placeholder': '- 없이 입력해주세요 (예시: 01012345678)'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
        }


class EditMyPage(forms.ModelForm):
    class Meta:
        model = User

        fields = ['email', 'phone', 'state', 'major']

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'text-end'}),
            'phone': forms.TextInput(
                attrs={'type': 'tel', 'pattern': "[0-9]{3}[0-9]{4}[0-9]{4}", 'class': 'text-end'}),
        }


# management

def find_pk(instance):
    pk = instance.pk
    return str(pk)


class ChangeUserGrade(forms.ModelForm):
    # grade = forms.ChoiceField(widget=forms.Select(attrs={'id': 'change-user-grade', 'onchange': 'SubmitForm('+ find_pk(instance) +')'}))

    class Meta:
        model = User

        fields = ['grade', 'username']

        widgets = {
            'username': forms.HiddenInput(),
        }

