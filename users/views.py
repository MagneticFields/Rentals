from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from users.models import CustomUser
from users.serializers.user_serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Api endpoint for viewing and editing users
    """

    queryset = CustomUser.objects.all().order_by('date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'patch', 'head', 'options']


