from rest_framework import serializers

from aicraft.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.
    """

    class Meta:
        model = Product
        fields = ['id', 'name', 'content', 'category', 'color', 'created',
                  'updated']
        read_only_fields = ['id', 'created', 'updated']
        # Meta class is used to provide metadata about the serializer.
        # It specifies the model (Product) and the fields to include in the serialization.
        # read_only_fields specifies fields that should not be modified directly.

    def create(self, validated_data):
        """
        Create and return a new Product instance.
        """
        # Custom implementation to create a new Product instance.
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Product instance.
        """
        # Custom implementation to update an existing Product instance.
        instance.name = validated_data.get('name', instance.name)
        instance.content = validated_data.get('content', instance.content)
        instance.category = validated_data.get('category', instance.category)
        instance.color = validated_data.get('color', instance.color)
        instance.save()
        return instance
