from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from aicraft.models import ProductSize
from aicraft.serializers.ProductSizeSerializer import ProductSizeSerializer


class ProductSizeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows viewing, creating, editing, and deleting ProductSizes.
    """
    queryset = ProductSize.objects.all()
    serializer_class = ProductSizeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
