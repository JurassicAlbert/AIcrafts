from rest_framework import serializers

from aicraft.models import ProductSite


class ProductSiteSerializer(serializers.ModelSerializer):
    """
    Serializer for the ProductSite model.
    """

    class Meta:
        model = ProductSite
        fields = ['id', 'name', 'product', 'company', 'product_size', 'product_pattern', 'price', 'url', 'created',
                  'updated']
        read_only_fields = ['id', 'created', 'updated']
        # Meta class is used to provide metadata about the serializer.
        # It specifies the model (ProductSite) and the fields to include in the serialization.
        # read_only_fields specifies fields that should not be modified directly.

    def validate_price(self, value):
        """
        Validates that the price is a positive value.
        """
        # Custom validation for the 'price' field to ensure it's a positive value.
        if value < 0:
            raise serializers.ValidationError("Price must be a positive value.")
        return value

    def create(self, validated_data):
        """
        Create and return a new ProductSite instance.
        """
        # Custom implementation to create a new ProductSite instance.
        return ProductSite.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing ProductSite instance.
        """
        # Custom implementation to update an existing ProductSite instance.
        instance.name = validated_data.get('name', instance.name)
        instance.product = validated_data.get('product', instance.product)
        instance.company = validated_data.get('company', instance.company)
        instance.product_size = validated_data.get('product_size', instance.product_size)
        instance.product_pattern = validated_data.get('product_pattern', instance.product_pattern)
        instance.price = validated_data.get('price', instance.price)
        instance.url = validated_data.get('url', instance.url)
        instance.save()
        return instance
