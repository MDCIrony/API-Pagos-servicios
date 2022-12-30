from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import ServicesSerializer
from .models import Services

from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated



class Rest_Services(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    # throttle_scope = 'all'
