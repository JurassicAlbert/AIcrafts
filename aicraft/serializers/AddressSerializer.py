from rest_framework import serializers

from aicraft.models import Address


class AddressSerializer(serializers.ModelSerializer):
    """
    Serializer for the Address model.
    """

    class Meta:
        model = Address
        fields = ['id', 'user', 'street', 'city', 'country', 'zip_code', 'is_default_delivery']
        read_only_fields = ['id']

    def create(self, validated_data):
        """
        Create and return a new Address instance.
        """
        return Address.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Address instance.
        """
        instance.street = validated_data.get('street', instance.street)
        instance.city = validated_data.get('city', instance.city)
        instance.country = validated_data.get('country', instance.country)
        instance.zip_code = validated_data.get('zip_code', instance.zip_code)
        instance.is_default_delivery = validated_data.get('is_default_delivery', instance.is_default_delivery)
        instance.save()
        return instance

    def __str__(self):
        return f"Address for {self.user.get_full_name()}"
