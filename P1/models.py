from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(default="")
    text = models.TextField(default="")
    std_id = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_name = models.CharField(max_length=200)


class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    std_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(default="")


class Post_Word(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    word = models.CharField(max_length=200)
