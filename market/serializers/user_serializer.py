from rest_framework import serializers

from market.models import User


class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100, allow_null=False)
    mobile_number = serializers.CharField(max_length=12, allow_null=False)
    email = serializers.CharField(max_length=30, allow_null=False)

    class Meta:
        model = User
        fields = ['__all__']
