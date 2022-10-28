from rest_framework import serializers
from .models import Serverapi

class ServerapiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serverapi
        fields = '__all__'