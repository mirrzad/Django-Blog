from django.urls import path
from . import views


urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog-list'),
    path('cat/<int:pk>/', views.BlogListView.as_view(), name='blog-list-category-filter'),
    path('detail/<int:pk>/', views.BlogDetailView.as_view(), name='blog-detail'),
    path('create-blog/', views.BlogCreateView.as_view(), name='blog-create'),
    path('detail/<int:pk>/edit/', views.BlogEditView.as_view(), name='blog-edit'),
    path('detail/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='blog-delete'),

]
