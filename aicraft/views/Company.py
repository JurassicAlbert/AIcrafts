from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from aicraft.models import Company
from aicraft.serializers.CompanySerializer import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows viewing, creating, editing, and deleting Company.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
