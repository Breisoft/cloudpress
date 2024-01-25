from rest_framework import serializers
from .models import Category, Comment, BlogPost


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name', 'updated']


"""

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment
        fields = ['user', 'body', 'created']
        read_only_fields = ['created']


class BlogPostSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = BlogPost
        fields = ['category', 'author', 'title']

"""
