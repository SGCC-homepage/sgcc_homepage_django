from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib import auth

from .forms import *
from .models import *


def main(request):
    return render(request, 'main.html')


def sign_up(request):
    form = CreateAccount()
    return render(request, 'sign_up.html', {'form': form})


def create_user(request):
    if request.method == "POST":
        print('회원가입')
        form = CreateAccount(request.POST)
        print(request.POST)
        if form.is_valid():
            print('유효')
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            if user.check_password(form.cleaned_data['password2']):
                user.save()
                auth.login(request, user)
                return redirect('main')
    else:
        form = CreateAccount()

    return render(request, 'sign_up.html', {'form': form})


def my_page(request):
    return render(request, 'my_page.html')