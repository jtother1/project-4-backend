from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    photo_url = models.TextField()
    about = models.TextField()

    def get_post_no(self):
        return self.posts.all().count()

    def __str__(self):
        return self.name
    