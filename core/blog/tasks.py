import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from celery import shared_task
from .models import Blog


@shared_task
def delete_deactivated_blogs():
    Blog.objects.filter(is_active=False).delete()

