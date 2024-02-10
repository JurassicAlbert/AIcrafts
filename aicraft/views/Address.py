from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from aicraft.models import Address
from aicraft.serializers.AddressSerializer import AddressSerializer


class AddressViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows viewing, creating, editing, and deleting Address.
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
