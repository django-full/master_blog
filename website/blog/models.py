from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse



class Autor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, )
    profile = models.ImageField()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('index')


class Post(models.Model):
    title = models.CharField(max_length=100)
    deskripsi = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    thum = models.ImageField(blank=True, null=True, )
    fuatured = models.BooleanField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'blog', kwargs={
                'blogger': self.id
            })

    @property
    def get_comments(self):
        return self.comments.all().order_by('-date')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=100)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
