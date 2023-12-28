from rest_framework import serializers
from .models import File

# to json
class SerializerFile(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'