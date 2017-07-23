from __future__ import absolute_import, unicode_literals
import random
from webb.celery import app
from celery.task.base import task


@task(name="recompute_blog_posts_words")
def compute_words(Post):
    Post.compute()
    return
