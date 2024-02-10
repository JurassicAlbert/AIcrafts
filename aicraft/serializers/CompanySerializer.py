from rest_framework import serializers

from aicraft.models import Company


class CompanySerializer(serializers.ModelSerializer):
    """
    Serializer for the Company model.
    """

    class Meta:
        model = Company
        fields = ['id', 'name', 'url']
        read_only_fields = ['id']

    def create(self, validated_data):
        """
        Create and return a new Company instance.
        """
        return Company.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Company instance.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.url = validated_data.get('url', instance.url)
        instance.save()
        return instance

    def __str__(self):
        return self.name
