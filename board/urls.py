from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('materials/', views.materials, name='materials'),
    path('reports/', views.reports, name='reports'),
    path('materials/add/', views.add_material, name='add_material'),
]