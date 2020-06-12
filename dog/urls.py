from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='posts_list'),
    path('post/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('comments/', views.PostList.as_view(), name='comments_list'),
    path('comment/<int:pk>', views.PostDetail.as_view(), name='comment_detail'),
]