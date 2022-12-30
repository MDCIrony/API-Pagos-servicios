from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .serializers import UserSerializer
from django.contrib.auth.models import User



from django.contrib.auth import get_user_model
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer




@api_view(['GET'])
def get_user(request, username):
    User = get_user_model()
    user = get_object_or_404(User, username=username)
    return Response({'id': user.id, 'is_staff':user.is_staff, 'username':user.username})
