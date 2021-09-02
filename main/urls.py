from django.urls import path
import main.views as views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', auth_views.LoginView.as_view(template_name='sign_in.html'), name='sign_in'),
    path('join/', views.sign_up, name='sign_up'),
    path('create/user/', views.create_user, name='create_user'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('mypage/', views.my_page, name='my_page'),
    path('mypage/edit/', views.my_page_edit, name='my_page_edit'),
    path('mypage/save/', views.my_page_save, name='my_page_save'),
]