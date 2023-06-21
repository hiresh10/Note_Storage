from rest_framework import serializers
from .models import Note

class Noteserializer(serializers.ModelSerializer):
    video = serializers.FileField(required=False)
    audio = serializers.FileField(required=False)
    class Meta:
        model = Note
        fields = '__all__'