from rest_framework import viewsets
from .models import File
from .serializers import SerializerFile

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = SerializerFile
    permission_classes = []
    authentication_classes = []