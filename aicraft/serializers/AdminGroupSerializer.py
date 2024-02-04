from django.contrib.auth.models import Group
from rest_framework import serializers


class AdminGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
