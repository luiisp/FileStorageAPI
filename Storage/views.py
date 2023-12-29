from rest_framework import viewsets
from .models import File
from .serializers import *

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    def get_serializer_class(self):
        if self.action == 'create':
            return FileCreateSerializer
        elif self.action == 'list':
            return FileListSerializer
        else:
            return FileListSerializer
    def perform_create(self, serializer):
        serializer.save()

