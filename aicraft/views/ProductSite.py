from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from aicraft.models import ProductSite
from aicraft.serializers.ProductSiteSerializer import ProductSiteSerializer


class ProductSiteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows viewing, creating, editing, and deleting ProductSites.
    """
    queryset = ProductSite.objects.all()
    serializer_class = ProductSiteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """
        Set the user field during the creation of a new ProductSite.
        """
        serializer.save(user=self.request.user)
