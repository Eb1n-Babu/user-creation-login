from .models import Accounts
from rest_framework import serializers

class account_detail_serializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = '__all__'
