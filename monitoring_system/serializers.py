from rest_framework import serializers
from monitoring_system.models import Resource, Collection


# class ResourceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Resource
#         fields = ('id', 'org_id', 'vm_id', 'date_time', 'value', 'metric_type')


# class PerDay(serializers.ModelSerializer):
#     class Meta:
#         model = Collection
#         fields = ('collection_time', 'id')


class PerDay(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()
   # day = serializers.SerializerMethodField()

    class Meta:
        model = Collection
        fields = ('id', 'collection_time', 'total')


    # Ask for more explanation
    def __init__(self, metric_type, *args, **kwargs):
        self._mtype = 'CPU'
        #self._mtype = metric_type
        super().__init__(*args, **kwargs)

    def get_total(self, obj):
        return obj.total(self._mtype)

    # def get_day(self, obj):
    #     hello = obj.total('CPU')
    #     next = hello/2
    #     return next