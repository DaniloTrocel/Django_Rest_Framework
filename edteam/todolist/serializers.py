from rest_framework import serializers
from .models import Tarea

class TareaSerializer(serializers.Serializer):
    descripcion = serializers.CharField(required=True)