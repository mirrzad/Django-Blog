from rest_framework import serializers
from ...models import Blog, Category
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ['id', 'title', 'category', 'is_active', 'content', 'author',
                  'created_date', 'updated_date']
        read_only_fields = ['author']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category'] = CategorySerializer(instance.category).data
        return rep

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author'] = User.objects.get(id=request.user.id)
        return super().create(validated_data)

