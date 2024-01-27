from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.RegisterApiView.as_view(), name='register-api'),
    path('token/login/', views.CustomLoginAuthToken.as_view(), name='login-token-api'),
    path('token/logout/', views.CustomDeleteAuthToken.as_view(), name='logout-token-api'),

    path('jwt/create-token/', TokenObtainPairView.as_view(), name='jwt-token-obtain-create'),
    path('jwt/refresh-token/', TokenRefreshView.as_view(), name='token-refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
