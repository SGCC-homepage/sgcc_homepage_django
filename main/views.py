from urllib import response
import requests
from rest_framework.generics import ListCreateAPIView, ListAPIView, GenericAPIView
from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import render, redirect
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.contrib.auth import views as auth_view

from api.user.models import JoinSGCC
from .forms import *
from api.user.serializers import RegisterSGCCSerializer

api_uri = getattr(settings, 'API_URI')

def main(request):
    return render(request, 'main.html')


class RegisterTemplateView(ListCreateAPIView):
    serializer_class = RegisterSGCCSerializer
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        form = CreateAccount()
        return Response({'form': form}, template_name='register.html')

    def post(self, request, *args, **kwargs):
        # print('회원가입')
        form = CreateAccount(request.POST)
        # print(request.POST)
        # print(form.is_valid())
        if form.is_valid():
            # print(form.cleaned_data)
            response = self.create(request, *args, **kwargs)
            if response.status_code == 201:
                return Response({'mss': 'welcome'}, template_name='register.html')
        return Response({'form': form}, template_name='register.html')


# mypage

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
    return render(request, 'mypage/my_page.html', {'user': user_info, 'grade': user.grade})


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
    return render(request, 'mypage/my_page_edit.html', {'user': user_info, 'form': form, 'grade': user.grade})


def my_page_save(request):
    user = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        form = EditMyPage(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('my_page')
    return redirect('my_page_edit')


# management
class UserManagementTemplateView(ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = User.objects.get(username=request.user.username)
            if user.grade == 4:
                # users = User.objects.all().order_by('name', 'username')
                users = User.objects.filter(grade__gt=0)
                users_list = get_user_list(users)
                return Response({'users': users_list, 'total': len(users), 'pay': len(users.filter(dues_payment=True)),
                                 'new': len(users.filter(grade=1)),
                                 'general': len(users.filter(grade=2)),
                                 'graduate': len(users.filter(grade=3))},
                                template_name='management/user_management.html')
        raise Http404('permission denied')


class RegisterManagementTemplateView(ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = User.objects.get(username=request.user.username)
            if user.grade == 4:
                # users = User.objects.all().order_by('name', 'username')
                users = User.objects.filter(grade=0)
                users_list = []
                i = 1
                for user in users:
                    join_sgcc = JoinSGCC.objects.get(user=user)
                    user_info = {
                        'index': i,
                        'pk': user.pk,
                        'name': user.name,
                        'username': user.username,
                        'major': user.get_major_display(),
                        'second_major': user.get_second_major_display(),
                        'third_major': user.get_third_major_display(),
                        'phone': user.phone,
                        'email': user.email,
                        'state': user.get_state_display(),
                        'is_authenticated': user.is_authenticated,
                        'reason': join_sgcc.reason,
                        'temp_demand': '예' if join_sgcc.temp_demand else '아니오',
                    }
                    users_list.append(user_info)
                    i += 1
                return Response({'users': users_list, 'total': len(users)},
                                template_name='management/register_management.html')
        raise Http404('permission denied')


def get_user_list(users):
    users_list = []
    i = 1
    for user in users:
        form = ChangeUserGrade(instance=user)
        user_info = {
            'index': i,
            'pk': user.pk,
            'name': user.name,
            'username': user.username,
            'major': user.get_major_display(),
            'phone': user.phone,
            'email': user.email,
            'state': user.get_state_display(),
            'grade': user.get_grade_display(),
            'dues_payment': '납' if user.dues_payment else '미납',
            'is_authenticated': user.is_authenticated,
            'form': form
        }
        users_list.append(user_info)
        i += 1
    return users_list


def delete_user(request):
    delete_users = User.objects.filter(grade=4)
    for user_query in delete_users:
        user_obj = User.objects.get(pk=user_query.pk)
        user_obj.delete()
    print('일괄 삭제 완료')
    return redirect('user_management')


def change_dues_payment(request):
    if request.method == "POST":
        form = request.POST
        username = form.get('username')
        user = User.objects.get(username=username)
        if user.dues_payment:
            user.dues_payment = False
        else:
            user.dues_payment = True
        user.save()
    return redirect('user_management')


def change_user_grade(request):
    if request.method == "POST":
        form = request.POST
        username = form.get('username')
        user = User.objects.get(username=username)
        user.grade = form.get('grade')
        user.save()
    return redirect('user_management')

def approve_users(request):
    if request.method == 'POST':
        form = request.POST
        users = User.objects.filter(grade=0)
        for user in users:
            if form.get(str(user.pk)) is None:
                continue
            user.grade = 1
            user.save()
    return redirect('register_management')