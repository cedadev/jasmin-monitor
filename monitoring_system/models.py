import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Collection(models.Model):
    """
    A collection of all resource records collected during the same 'collection phase'.
    """
    # Commenting for the generation of fake data
    #collection_time = models.DateTimeField(auto_now_add=True)


    collection_time = models.DateTimeField('date published')

    class Meta:
        ordering = ['collection_time']


    # def total(self, metric_type):
    #     total = 0
    #     for r in self.resource_set.filter(metric_type=metric_type).all():
    #         total += int(r.value)
    #     return total


        # This works
        # for r in Resource.objects.filter(collection = self, metric_type = metric_type).all():
        #     total += int(r.value)
        # return total


class Resource(models.Model):
    CPU = 'CPU'
    RAM = 'RAM'
    __MetricType =(
        (CPU, 'CPU Cores'),
        (RAM, 'RAM Used'),
    )

    collection = models.ForeignKey(Collection)
    org_id = models.CharField(max_length=50)
    vm_id = models.CharField(max_length=50)
    value = models.IntegerField()
    metric_type = models.CharField(max_length=3, choices=__MetricType)

    def __str__(self):
         return self.org_id

