# serializers.py

from rest_framework import serializers

from .ProductSerializer import ProductSerializer
from ..models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Payment model.
    """
    product = ProductSerializer()  # Dodaj odpowiedni serializer dla modelu Product

    class Meta:
        model = Payment
        fields = ['id', 'user', 'product', 'quantity', 'payment_type', 'is_successful']
        read_only_fields = ['id']

    def create(self, validated_data):
        """
        Create and return a new Payment instance.
        """
        return Payment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Payment instance.
        """
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.payment_type = validated_data.get('payment_type', instance.payment_type)
        instance.is_successful = validated_data.get('is_successful', instance.is_successful)
        instance.save()
        return instance

    def validate_quantity(self, value):
        """
        Validate that the quantity is a positive integer.
        """
        if value <= 0:
            raise serializers.ValidationError("Quantity must be a positive integer.")
        return value

    def __str__(self):
        return f"{self.user.get_full_name()}'s Payment for {self.product.name}"
