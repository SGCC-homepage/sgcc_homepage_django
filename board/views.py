from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import *
from .models import *


def materials(request):
    all_category = Category.objects.all()
    materials = []
    for category in all_category:
        category_dict = {'category': category.name}
        materials_of_category = Material.objects.filter(main_category__name=category.name)
        category_dict['contents'] = materials_of_category
        materials.append(category_dict)
    return render(request, 'materials.html', {'materials': materials})


''' materials structure
[
    {
        'category': 'python',
        'contents': QuerySet<Material>
    },
    ...
]
'''

def reports(request):
    mss = ''

    if request.method == "POST":
        form = request.POST
        file = request.FILES
        print(form, file)
        team = form.get('team')
        if team == '-1':
            print('팀 생성')
            team_obj = Team(name=form.get('add_team'))
            team_obj.save()
        else:
            if len(Team.objects.filter(name=team)) == 1:
                print('팀 발견')
                team_obj = Team.objects.get(name=team)
            else:
                mss = '팀명을 다시 확인해주세요'
        if len(Report.objects.filter(title=form.get('title'), team=team_obj)) == 0:
            report_obj = Report(title=form.get('title'), team=team_obj, report=file.get('report'))
            report_obj.save()
        else:
            report_obj = Report.objects.get(title=form.get('title'), team=team_obj)
            report_obj.report = file.get('report')
            report_obj.save()
            mss = '보고서가 덮어씌워졌습니다'

    all_reports = Report.objects.all()
    reports = []
    for report in all_reports:
        report_info = {
            'title': report.title,
            'team': report.team.name,
            'date': report.date.strftime("%Y.%m.%d"),
            'report': report.report
        }
        reports.append(report_info)
    all_teams = Team.objects.all()

    return render(request, 'reports.html', {'reports': reports, 'teams': all_teams, 'mss': mss})


def add_material(request):
    if request.method == "POST":
        form = request.POST
        print(form)
        main_category = form.get('main_category')
        if main_category == '-1':
            new_category = form.get('add_main_category')
            if len(Category.objects.filter(name=new_category)) == 0:
                category_obj = Category(name=new_category)
                category_obj.save()
                Material.objects.create(main_category=category_obj, contents=form.get('contents'))
                return redirect('materials')
            else:
                main_category = new_category
        if len(Category.objects.filter(name=main_category)) == 1:
            category_obj = Category.objects.get(name=main_category)
            Material.objects.create(main_category=category_obj, contents=form.get('contents'))
            return redirect('materials')
    return render(request, 'materials.html', {'mss': '생성 실패'})