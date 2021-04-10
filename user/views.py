from django.contrib.auth import authenticate
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib import auth

from .forms import *
from .models import *


def main(request):
    return render(request, 'main.html')


def sign_up(request):
    if User.objects.filter(username=request.user.username):
        user = User.objects.get(username=request.user.username)
        if user.grade == 2:
            form = CreateAccount()
            return render(request, 'sign_up.html', {'form': form})
        else:
            raise Http404('permission denied')
    else:
        raise Http404('permission denied')



def create_user(request):
    if request.method == "POST":
        print('회원가입')
        form = CreateAccount(request.POST)
        print(request.POST)
        if form.is_valid():
            print('유효')
            user = form.save(commit=False)
            user.student_id = user.username
            user.set_password(form.cleaned_data['password1'])
            if user.check_password(form.cleaned_data['password2']):
                user.save()
                auth.login(request, user)
                return render(request, 'main.html', {'mss': 'welcome'})
    else:
        form = CreateAccount()

    return render(request, 'sign_up.html', {'form': form})


def my_page(request):
    print(request.user.username)
    user = User.objects.get(username=request.user.username)
    user_info = {
        'pk': user.pk,
        'name': user.name,
        'major': user.get_major_display(),
        'phone': user.phone,
        'email': user.email,
        'student_id': user.student_id,
        'state': user.get_state_display(),
        'grade': user.get_grade_display(),
        'dues_payment': '납' if user.dues_payment else '미납',
        'is_authenticated': user.is_authenticated
    }
    return render(request, 'my_page.html', {'user': user_info, 'grade': user.grade})


def my_page_edit(request):
    user = User.objects.get(username=request.user.username)
    form = EditMyPage(instance=user)
    user_info = {
        'pk': user.pk,
        'name': user.name,
        'major': user.get_major_display(),
        'phone': user.phone,
        'email': user.email,
        'student_id': user.student_id,
        'state': user.get_state_display(),
        'grade': user.get_grade_display(),
        'dues_payment': '납' if user.dues_payment else '미납',
        'is_authenticated': user.is_authenticated
    }
    return render(request, 'my_page_edit.html', {'user': user_info, 'form': form, 'grade': user.grade})


def my_page_save(request):
    user = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        form = EditMyPage(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('my_page')
    return redirect('my_page_edit')