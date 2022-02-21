from django.urls import path
import main.views as views
from main.views import RegisterTemplateView, UserManagementTemplateView, RegisterManagementTemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', auth_views.LoginView.as_view(template_name='sign_in.html'), name='sign_in'),
    # path('join/', views.register, name='register'),
    path('join/', RegisterTemplateView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # mypage
    path('mypage/', views.my_page, name='my_page'),
    path('mypage/edit/', views.my_page_edit, name='my_page_edit'),
    path('mypage/save/', views.my_page_save, name='my_page_save'),

    # management
    path('management/user/', UserManagementTemplateView.as_view(), name='user_management'),
    path('management/user/register/', RegisterManagementTemplateView.as_view(), name='register_management'),
    path('user/delete/', views.delete_user, name='delete_user'),
    path('change/dues/payment/', views.change_dues_payment, name='change_dues_payment'),
    path('change/user/grade/', views.change_user_grade, name='change_user_grade'),
    path('approve/users/', views.approve_users, name='approve_users'),
]