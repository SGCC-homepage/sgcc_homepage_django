from django.shortcuts import render, redirect
from django.http import Http404

from user.models import *
from .forms import *


def user_management(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        if user.grade == 2:
            # users = User.objects.all().order_by('name', 'username')
            users = User.objects.all().order_by('name', 'username')
            users_list = []
            i = 1
            for user in users:
                form = ChangeUserGrade(instance=user)
                user_info = {
                    'index': i,
                    'pk': user.pk,
                    'name': user.name,
                    'student_id': user.username,
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
                i+=1
            return render(request, 'user_management.html', {'users': users_list})
        else:
            raise Http404('permission denied')
    else:
        raise Http404('permission denied')


def delete_user(request):
    delete_users = User.objects.filter(grade=4)
    for user_query in delete_users:
        user_obj = User.objects.get(pk=user_query.pk)
        user_obj.delete()
    print('일괄 삭제 완료')
    return redirect('user_management')


dummy_users = [
    {
        'pk': 0,
        'name': '이름1',
        'student_id': '20190258',
        'major': '유럽문화학과',
        'phone': '01012345678',
        'email': 'exam1234@gmail.com',
        'state': '재학',
        'grade': '운영진',
        'dues_payment': 'true',
    },
    {
        'pk': 1,
        'name': '이름2',
        'student_id': '20200258',
        'major': '국어국문학과',
        'phone': '01012345678',
        'email': 'exam1234@gmail.com',
        'state': '재학',
        'grade': '운영진',
        'dues_payment': 'true',
    },
    {
        'pk': 2,
        'name': '이름3',
        'student_id': '20190858',
        'major': '전자공학과',
        'phone': '01012345678',
        'email': 'exam1234@gmail.com',
        'state': '재학',
        'grade': '신입',
        'dues_payment': 'true',
    },
    {
        'pk': 3,
        'name': '이름4',
        'student_id': '20190256',
        'major': '경제학과',
        'phone': '01085219632',
        'email': 'exam1789@gmail.com',
        'state': '재학',
        'grade': '일반',
        'dues_payment': 'false',
    },
    {
        'pk': 4,
        'name': '이름5',
        'student_id': '20190256',
        'major': '철학과',
        'phone': '01079851324',
        'email': 'exam7854)@gmail.com',
        'state': '교환',
        'grade': '비활',
        'dues_payment': 'false',
    },
    {
        'pk': 5,
        'name': '이름6',
        'student_id': '201401154',
        'major': '정치외교학',
        'phone': '01074158965',
        'email': 'exam!!78@gmail.com',
        'state': '재학',
        'grade': '탈퇴',
        'dues_payment': 'false',
    }
]


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
