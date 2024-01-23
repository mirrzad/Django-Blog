from django.contrib import admin
from .models import Blog, Category


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'is_active', 'created_date']
    list_filter = ['is_active', 'created_date', 'author']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['created_date']


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
