from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    comments = serializers.StringRelatedField(many=True)
    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'body', 'updated', 'created', 'comments',]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'body', 'post', 'updated', 'created', 'active',]