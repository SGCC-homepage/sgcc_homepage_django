from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.user_management, name='user_management'),
    path('user/delete/', views.delete_user, name='delete_user'),
]