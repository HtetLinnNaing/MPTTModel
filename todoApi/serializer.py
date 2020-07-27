from todoApi.models import todo
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = todo
        fields = ['id', 'name', 'done', 'created_at']
