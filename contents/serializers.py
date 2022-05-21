from rest_framework import serializers
from .models import ContentManagement

class NoteContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentManagement
        fields = ['heading', 'body', 'created_at']