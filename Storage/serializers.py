from rest_framework import serializers
import os
import datetime
from .models import File
from django.conf import settings

class FileCreateSerializer(serializers.ModelSerializer):
    fullFile = serializers.FileField(source='full_file')
    class Meta:
        model = File
        fields = ['title','fullFile']

class FileListSerializer(serializers.ModelSerializer):
    readSize = serializers.SerializerMethodField()
    meta = serializers.SerializerMethodField()
    uploadedAt = serializers.DateTimeField(source='uploaded_at',format="%Y-%m-%dT%H:%M:%S.%fZ", read_only=True)
    fileUrl = serializers.FileField(source='full_file')

    class Meta:
        model = File
        fields = ('id','title' ,'fileUrl','readSize','uploadedAt','meta')

    def get_readSize(self, obj):
        path = os.path.join(settings.MEDIA_ROOT, f'{obj.full_file}')
        size = os.path.getsize(path)
        for u in ['B', 'KB', 'MB', 'GB']:
            if size < 1024.0:
                break
            size /= 1024.0
        return f"{size:.2f} {u}"
    
    def get_meta(self, obj):
        path = os.path.join(settings.MEDIA_ROOT, f'{obj.full_file}')
        return {
            'name': obj.full_file.name,
            'size': os.path.getsize(path),
            'format': obj.full_file.name.split('.')[-1],
            'created': datetime.datetime.fromtimestamp(os.path.getctime(path))
        }
