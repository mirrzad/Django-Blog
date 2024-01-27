import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from blog.models import Blog, Category


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def sample_user():
    user = User.objects.create(username='test', password='test@123456')
    return user


@pytest.fixture
def sample_category():
    cat = Category.objects.create(title='cat-test')
    return cat


@pytest.fixture
def sample_blog(sample_user, sample_category):
    blog = Blog.objects.create(
        title='test blog',
        content='test',
        is_active=True,
        author=sample_user,
        category=sample_category
    )
    return blog


@pytest.mark.django_db
class TestBlogApi:

    def test_get_blog_list(self, api_client, sample_user):
        api_client.force_authenticate(user=sample_user)
        url = reverse('blog-list-api')
        response = api_client.get(url)
        assert response.status_code == 200

    def test_get_blog_list_without_auth(self, api_client):
        url = reverse('blog-list-api')
        response = api_client.get(url)
        assert response.status_code == 401

    def test_create_blog(self, api_client, sample_user, sample_category):
        api_client.force_authenticate(user=sample_user)
        url = reverse('blog-list-api')
        category = sample_category
        data = {
            'title': 'test blog',
            'content': 'test',
            'is_active': True,
            'category': category.id
        }
        response = api_client.post(url, data)
        assert response.status_code == 201
        assert Blog.objects.get(pk=response.data.get('id')).id == response.data.get('id')

    def test_create_blog_without_auth(self, api_client):
        url = reverse('blog-list-api')
        data = {
            'title': 'test blog',
            'content': 'test',
            'is_active': True,
        }
        response = api_client.post(url, data)
        assert response.status_code == 401

    def test_get_blog_item(self, sample_user, api_client, sample_blog):
        api_client.force_authenticate(user=sample_user)
        url = reverse('blog-detail-api', kwargs={'pk': sample_blog.id})
        response = api_client.get(url)
        assert response.status_code == 200

    def test_update_blog_item(self, sample_user, api_client, sample_blog, sample_category):
        api_client.force_authenticate(user=sample_user)
        url = reverse('blog-detail-api', kwargs={'pk': sample_blog.id})
        category = sample_category
        data = {
            'title': 'test blog test',
            'content': 'test',
            'is_active': False,
            'category': category.id
        }
        response = api_client.put(url, data)
        assert response.status_code == 200

    def test_update_partial_blog_item(self, sample_user, api_client, sample_blog, sample_category):
        api_client.force_authenticate(user=sample_user)
        url = reverse('blog-detail-api', kwargs={'pk': sample_blog.id})
        category = sample_category
        data = {
            'is_active': False,
        }
        response = api_client.patch(url, data)
        assert response.status_code == 200

    def test_delete_blog_item(self, sample_user, api_client, sample_blog):
        api_client.force_authenticate(user=sample_user)
        url = reverse('blog-detail-api', kwargs={'pk': sample_blog.id})
        response = api_client.delete(url)
        assert response.status_code == 204

