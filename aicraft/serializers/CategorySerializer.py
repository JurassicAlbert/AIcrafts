from rest_framework import serializers

from aicraft.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.
    """

    class Meta:
        model = Category
        fields = ['id', 'name']
        read_only_fields = ['id']

    def create(self, validated_data):
        """
        Create and return a new Category instance.
        """
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Category instance.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

    def __str__(self):
        return self.name
