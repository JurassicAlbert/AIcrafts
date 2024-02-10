from rest_framework import serializers

from aicraft.models import Pattern


class PatternSerializer(serializers.ModelSerializer):
    """
    Serializer for the Pattern model.
    """

    class Meta:
        model = Pattern
        fields = ['id', 'name', 'code', 'color', 'created', 'updated']
        read_only_fields = ['id', 'created', 'updated']

    def create(self, validated_data):
        """
        Create and return a new Pattern instance.
        """
        return Pattern.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Pattern instance.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.code = validated_data.get('code', instance.code)
        instance.color = validated_data.get('color', instance.color)
        instance.save()
        return instance

    def __str__(self):
        return self.name
