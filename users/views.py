from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class RegistrationAPIView(APIView):
    
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # This method will return the serialized representations of new refresh
            #  and access tokens for the given user.
            refresh = RefreshToken.for_user(user)
            res = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
            return Response(res, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer