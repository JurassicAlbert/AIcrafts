from django.contrib.auth.models import Group
from rest_framework import permissions, viewsets

from aicraft.serializers.AdminGroupSerializer import AdminGroupSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = AdminGroupSerializer
    permission_classes = [permissions.IsAuthenticated]
