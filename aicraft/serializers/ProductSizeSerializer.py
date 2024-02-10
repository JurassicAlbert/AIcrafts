from rest_framework import serializers

from aicraft.models import ProductSize


class ProductSizeSerializer(serializers.ModelSerializer):
    """
    Serializer for the ProductSize model.
    """

    class Meta:
        model = ProductSize
        fields = ['id', 'name', 'chest_circumference', 'height', 'sleeve_height', 'person_height']
        read_only_fields = ['id']

    def create(self, validated_data):
        """
        Create and return a new ProductSize instance.
        """
        return ProductSize.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing ProductSize instance.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.chest_circumference = validated_data.get('chest_circumference', instance.chest_circumference)
        instance.height = validated_data.get('height', instance.height)
        instance.sleeve_height = validated_data.get('sleeve_height', instance.sleeve_height)
        instance.person_height = validated_data.get('person_height', instance.person_height)
        instance.save()
        return instance

    def __str__(self):
        return self.name
