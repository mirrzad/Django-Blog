from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ...models import Blog
from .serializers import BlogSerializer


class BlogListApi(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Blog.objects.filter(is_active=True)
    serializer_class = BlogSerializer


class BlogDetailApi(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BlogSerializer
    queryset = Blog.objects.filter(is_active=True)

    
