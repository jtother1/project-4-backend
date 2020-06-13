from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', include('dog.urls')),
    path('', include('profiles.urls')),

]
