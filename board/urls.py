from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('materials/', views.materials, name='materials'),
    path('questions/', views.questions, name='questions'),
]