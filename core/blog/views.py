from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Blog, Category
from .forms import BlogForm
from django.urls import reverse


class BlogListView(ListView, LoginRequiredMixin):
    template_name = 'blog/blog-list.html'
    model = Blog
    paginate_by = 4
    context_object_name = 'blogs'

    def get_queryset(self, **kwargs):
        if self.kwargs.get('pk') is None:
            query = Blog.objects.filter(is_active=True).select_related('category', 'author')
        else:
            query = Blog.objects.filter(category__id=self.kwargs.get('pk'), is_active=True)\
                .select_related('category', 'author')
        return query

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class BlogDetailView(DetailView, LoginRequiredMixin):
    template_name = 'blog/blog-detail.html'
    model = Blog
    context_object_name = 'blog'

    def get_queryset(self):
        query = super().get_queryset()
        query.filter(is_active=True).select_related('author').prefetch_related('comments')
        return query


class BlogCreateView(CreateView, LoginRequiredMixin):
    form_class = BlogForm
    template_name = 'blog/blog-form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog-list')


class BlogEditView(UpdateView, LoginRequiredMixin):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/blog-edit-form.html'

    def get_success_url(self):
        return reverse('blog-list')


class BlogDeleteView(DeleteView, LoginRequiredMixin):
    model = Blog
    template_name = 'blog/blog-confirm-delete.html'
    context_object_name = 'blog'

    def get_success_url(self):
        return reverse('blog-list')
