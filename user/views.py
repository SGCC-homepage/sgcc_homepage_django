from django.shortcuts import render

from .forms import *
from .models import *


def main(request):
    REST_API_KEY = 'd993887a2f7194c865cec5fbff6727b1'
    REDIRECT_URI = "http://127.0.0.1:8000/account/login/kakao/redirect"
    kakao_login_url = f"https://kauth.kakao.com/oauth/authorize?client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&response_type=code"
    return render(request, 'main.html', {'kakao_login': kakao_login_url})


def sign_in(request):
    form = LogIn()
    return render(request, 'sign_in.html', {'form': form})


def sign_up(request):
    form = CreateAccount()
    return render(request, 'sign_up.html', {'form': form})