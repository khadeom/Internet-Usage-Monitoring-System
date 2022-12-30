from rest_framework import serializers
from .models import UserData

class UserDataSerializer(serializers.ModelSerializer):
    last_day = serializers.DurationField(source='usage_time')
    last_week = serializers.DurationField(source='usage_time')
    last_month = serializers.DurationField(source='usage_time')

    class Meta:
        model = UserData
        fields = ('username', 'last_day', 'last_week', 'last_month')

class InternetUsageSerializer(serializers.Serializer):
    username = serializers.CharField()
    usage_1day = serializers.DurationField()
    usage_7days = serializers.DurationField()
    usage_30days = serializers.DurationField()