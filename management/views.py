from django.shortcuts import render, redirect

from user.models import *


def user_management(request):
    return render(request, 'user_management.html', {'users': dummy_users})


def read_user(request):
    users = User.objects.all()
    print(users)

    users = User.objects.values()
    print(users)

    # 이름 기준 오름차순 정렬
    users = User.objects.values().order_by('name')
    print(users)

    # 이름 기준 내림차순 정렬
    users = User.objects.values().order_by('-name')
    print(users)

    return render(request, 'user_management.html', {'users':users})


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