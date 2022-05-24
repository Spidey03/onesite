from rest_framework import serializers

from market.models import SiteModel


class SiteSerializer(serializers.Serializer):
    owner_id = serializers.CharField(allow_null=False)
    street_name = serializers.CharField(allow_null=False, max_length=1000)
    village = serializers.CharField(allow_null=False, max_length=1000)
    city = serializers.CharField(allow_null=False, max_length=1000)
    district = serializers.CharField(allow_null=False, max_length=1000)
    state = serializers.CharField(allow_null=False, max_length=1000)
    country = serializers.CharField(allow_null=False, max_length=1000)

    class Meta:
        model = SiteModel
        fields = ['__all__']
