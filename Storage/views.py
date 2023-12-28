from django.http import HttpResponse
from rest_framework import generics, viewsets
from django.contrib.auth.models import User
from .models import File
from .serializers import SerializerFile, SerializerUser

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = SerializerFile
    permission_classes = []
    authentication_classes = []

class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SerializerUser
    permission_classes = []
    authentication_classes = []

class FileDownloadAPIView(generics.RetrieveAPIView):
    queryset = File.objects.all()
    serializer_class = SerializerFile

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        file_path = instance.full_file.path

        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{instance.full_file.name}"'
            return response
