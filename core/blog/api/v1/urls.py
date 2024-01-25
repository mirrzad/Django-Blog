from django.urls import path
from . import views


urlpatterns = [
    path('blog-list/', views.BlogListApi.as_view(), name='blog-list-api'),
    path('blog-detail/<int:pk>/', views.BlogDetailApi.as_view(), name='blog-detail-api'),

]
