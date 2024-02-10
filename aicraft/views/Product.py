from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from aicraft.models import Product
from aicraft.serializers.ProductSerializer import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows viewing, creating, editing, and deleting Product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
