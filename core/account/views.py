from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterPageView(CreateView):
    template_name = 'account/register-page.html'
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse('login-page')


class LoginPageView(LoginView):
    template_name = 'account/login-page.html'
    form_class = AuthenticationForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('blog-list')


class LogoutPageView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login-page'))
