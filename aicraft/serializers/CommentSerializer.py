from rest_framework import serializers

from aicraft.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model.
    """

    class Meta:
        model = Comment
        fields = ['id', 'title', 'content', 'product', 'user', 'created', 'updated']
        read_only_fields = ['id', 'created', 'updated']

    def create(self, validated_data):
        """
        Create and return a new Comment instance.
        """
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Comment instance.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance

    def __str__(self):
        return self.title
