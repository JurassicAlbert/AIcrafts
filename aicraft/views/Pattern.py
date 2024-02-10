from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from aicraft.models import Pattern
from aicraft.serializers.PatternSerializer import PatternSerializer


class PatternViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows viewing, creating, editing, and deleting Pattern.
    """
    queryset = Pattern.objects.all()
    serializer_class = PatternSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
