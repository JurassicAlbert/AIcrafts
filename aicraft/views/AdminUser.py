from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

from aicraft.serializers.AdminUserSerializer import AdminUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = AdminUserSerializer
    permission_classes = [permissions.IsAuthenticated]
