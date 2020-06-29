from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from .models import loaCrawling


class loaSerializer(serializers.ModelSerializer):
    class Meta:
        model = loaCrawling
        fields = '__all__'
