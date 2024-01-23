from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Blog
from .forms import BlogForm
from django.urls import reverse


class BlogListView(ListView):
    template_name = 'blog/blog-list.html'
    model = Blog
    paginate_by = 3
    context_object_name = 'blogs'
    ordering = "-id"

    def get_queryset(self):
        query = Blog.objects.filter(is_active=True).select_related('category', 'author')
        return query


class BlogDetailView(DetailView):
    template_name = 'blog/blog-detail.html'
    model = Blog
    context_object_name = 'blog'

    def get_queryset(self):
        query = super().get_queryset()
        query.filter(is_active=True).select_related('author')
        return query


class BlogCreateView(CreateView):
    form_class = BlogForm
    template_name = 'blog/blog-form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog-list')


class BlogEditView(UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/blog-edit-form.html'

    def get_success_url(self):
        return reverse('blog-list')


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/blog-confirm-delete.html'
    context_object_name = 'blog'

    def get_success_url(self):
        return reverse('blog-list')
