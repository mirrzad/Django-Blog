from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginPageView.as_view(), name='login-page'),
    path('register/', views.RegisterPageView.as_view(), name='register-page'),
]
