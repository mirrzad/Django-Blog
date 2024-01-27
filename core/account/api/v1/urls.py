from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.RegisterApiView.as_view(), name='register-api')
]

