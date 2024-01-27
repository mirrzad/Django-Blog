from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from ...models import Blog
from .serializers import BlogSerializer


class BlogListApi(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    # queryset = Blog.objects.filter(is_active=True)
    serializer_class = BlogSerializer

    def get_queryset(self, **kwargs):
        if self.kwargs.get('pk') is None:
            query = Blog.objects.filter(is_active=True)
        else:
            query = Blog.objects.filter(is_active=True, category__id=self.kwargs.get('pk'))
        return query


class BlogDetailApi(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BlogSerializer
    queryset = Blog.objects.filter(is_active=True)


