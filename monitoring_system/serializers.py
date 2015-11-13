from rest_framework import serializers
from monitoring_system.models import Resource


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ('id', 'org_id', 'vm_id', 'date_time', 'value', 'metric_type')


class PerDay(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ('date_time', 'value')