from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView


class RegisterPageView(LoginView):
    template_name = 'account/register-page.html'


class LoginPageView(LoginView):
    template_name = 'account/login-page.html'
