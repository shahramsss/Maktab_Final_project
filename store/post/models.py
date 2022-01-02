from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import PROTECT


class Category(models.Model):
    title = models.CharField(max_length=56)
    # parent = models.ForeignKey(
    #     "self", null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=56)
    image_address = models.ImageField(
        upload_to='templates/images', blank=True, null=True)

    def __str__(self) -> str:
        return self.title


class Tag (models.Model):
    title = models.CharField(max_length=56)

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    title = models.CharField('title', max_length=56, unique=True)
    description = models.TextField()
    short_description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    writer = models. ForeignKey(User, on_delete=models.DO_NOTHING)
    category = models.ManyToManyField(Category)
    slug = models.SlugField(unique=True, null=False)
    tag = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return f'{self.title} {self.writer}'


class Comment(models.Model):
    title = models.CharField(max_length=56)
    text = models.TextField('commnet text')
    created_at = models.DateTimeField(auto_now_add=True)
    # author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f'{self.text[:10]}-{self.author}-{self.post}'
