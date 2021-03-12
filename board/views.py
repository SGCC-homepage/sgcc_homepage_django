from django.shortcuts import render


def materials(request):
    return render(request, 'materials.html')
