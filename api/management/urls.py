from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.user_management, name='user_management'),
    path('user/delete/', views.delete_user, name='delete_user'),
    path('change/dues/payment/', views.change_dues_payment, name='change_dues_payment'),
    path('change/user/grade/', views.change_user_grade, name='change_user_grade'),
]