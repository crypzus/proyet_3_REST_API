from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description','technology', 'create_at')
        # este comando es para que el campo que se especifica sea solo lectura 
        read_only_fields = ('create_at')