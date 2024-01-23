from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    image = models.ImageField(upload_to="blog/", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="blogs", null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="blogs")
    is_active = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.title

