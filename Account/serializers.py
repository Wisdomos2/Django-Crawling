from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        # 모델 User의 모든 field를 serializer함.
