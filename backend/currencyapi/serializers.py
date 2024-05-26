from .models import *
from rest_framework import serializers
from decimal import Decimal




class CurrencySerializer(serializers.ModelSerializer):
    value = serializers.DecimalField(max_digits=8, decimal_places=5)
    class Meta:
        model = Currency
        fields = ["code", "name", "nominal", "value"]
    