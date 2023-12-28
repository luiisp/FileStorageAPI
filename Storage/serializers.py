from rest_framework import serializers, viewsets
from django.contrib.auth.models import User
from .models import File

# to json
class SerializerFile(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

class SerializerUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
