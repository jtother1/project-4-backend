from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    photo_url = models.TextField()
    about = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=250)

    def __str__(self):
        return self.author


class Comment(models.Model):
    author = models.CharField(max_length=100)
    body = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment")

    def __str__(self):
        return self.author
