from django.shortcuts import render


def materials(request):
    return render(request, 'materials.html')


def questions(request):
    return render(request, 'qusetions.html')