from rest_framework import serializers
from .models import Calculatorapi

class CalculatorInputSerializer(serializers.Serializer):
    operation_type = serializers.CharField(write_only=True, required=True)
    x = serializers.FloatField(required=False)
    y = serializers.FloatField(required=False)
