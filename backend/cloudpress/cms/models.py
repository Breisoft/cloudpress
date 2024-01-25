from django.db import models

from django.conf import settings

# Create your models here.


class Category(models.Model):
    name = models.TextField()

    updated = models.DateTimeField(auto_now=True)


class BlogPost(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    title = models.TextField()
    slug = models.SlugField()

    created = models.DateTimeField()
    updated = models.DateTimeField(auto_now=True)

    def _set_slug(self):
        # TODO set slug
        pass


class Comment(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    body = models.TextField(max_length=512)

    created = models.DateTimeField()
    updated = models.DateTimeField(auto_now=True)
