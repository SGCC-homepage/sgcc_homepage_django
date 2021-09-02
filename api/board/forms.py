from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *


class CreateMaterialForm(forms.Form):
    main_category = forms.CharField()
    add_main_category = forms.CharField()
    contents = forms.CharField()
