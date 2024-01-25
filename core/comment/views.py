from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView
from .models import Comment
from .forms import CommentForm
from blog.models import Blog


class CommentCreateView(CreateView, LoginRequiredMixin):
    model = Comment
    form_class = CommentForm
    template_name = 'comment/comment-form.html'

    def form_valid(self, form, **kwargs):
        form.instance.user = self.request.user
        form.instance.blog = Blog.objects.get(pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog-list')
