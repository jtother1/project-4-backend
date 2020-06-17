from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth import get_user_model
from profiles.models import Profile

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=300)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    
    
    
    

    def __str__(self):
        return self.title

    def num_comments(self):
        return self.comment_set.all().count()

class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
    body = models.TextField(max_length=300, default="blank")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.user)



