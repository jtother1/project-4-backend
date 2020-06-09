from rest_framework import serializers
from .models import User, Post, Comment

class UserSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'photo_url','about',]

class PostSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.HyperlinkedRelatedField(
        view_name='post_detail',
        many=True,
        read_only=True

    )
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'body',]

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    comment = serializers.HyperlinkedRelatedField(
        view_name='comment_detail',
        many=True,
        read_only=True

    )
    class Meta:
        model = Comment
        fields = ['id', 'author', 'title', 'body',]