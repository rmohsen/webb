from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Post(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(default="")
    text = models.TextField(default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    length = models.IntegerField()

    def __str__(self):
        return str(self.id)

    def compute_post(self):
        import re
        l = list()
        l = re.compile('\w+').findall(self.title) + re.compile('\w+').findall(self.summary) + re.compile(
            '\w+').findall(self.text)
        for word in l:
            p = Post_Word.objects.filter(post=self).get(word=word)
            if p is None:
                Post_Word.objects.create(Post=self, count=1, word=word)
            else:
                p.count += 1
            p.save()
        self.length = len(l)
        return


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(default="")

    def __str__(self):
        return str(self.id)


class Post_Word(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    word = models.CharField(max_length=200)
    count = models.IntegerField()

    def __str__(self):
        return str(str(self.post.id) + str(self.word))


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


@receiver(post_save, sender=Post)
def update_post(sender, instance, **kwargs):
    from .task import compute_words
    compute_words(instance.Post)
    return
