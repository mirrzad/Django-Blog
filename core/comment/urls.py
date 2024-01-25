from django.urls import path
from . import views


urlpatterns = [
    path('create-comment/<int:pk>/', views.CommentCreateView.as_view(), name='comment-create')
]

