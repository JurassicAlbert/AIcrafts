from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from aicraft.models import Category
from aicraft.serializers.CategorySerializer import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows viewing, creating, editing, and deleting Category.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
