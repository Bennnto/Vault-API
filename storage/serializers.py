from rest_framework import serializers
from .models import Storage, Tags

class StorageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, allow_null=True)
    
    class Meta:
        model = Storage
        fields = ['id', 'label', 'description', 'function', 'link', 'image', 'tags', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['id', 'tag_name', 'user']
        read_only_fields = ['id', 'user']