from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .serializers import CategorySerializer
from .models import BlogPost, Comment, Category


# Create your views here.

class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


"""
class BlogPostViewSet(ModelViewSet):
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()


class CommentView(ModelViewSet):

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
"""
