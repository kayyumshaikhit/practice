from rest_framework import serializers
from .models import fileModel

class fileSerializer(serializers.ModelSerializer):
    class Meta:
        model = fileModel
        fields = "__all__"
