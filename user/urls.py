from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.sign_in, name='sign_in'),
    path('join/', views.sign_up, name='sign_up'),
]