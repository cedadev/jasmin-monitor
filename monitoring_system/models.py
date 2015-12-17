import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Collection(models.Model):
    """
    A collection of all resource records collected during the same 'collection phase'.
    """
    # Comment this out if need to generate fake data
    collection_time = models.DateTimeField(auto_now_add=True)

    # Uncomment this to generate fake data
    #collection_time = models.DateTimeField('date published')

    class Meta:
        ordering = ['collection_time']

class Resource(models.Model):
    CPU = 'CPU'
    RAM = 'RAM'
    __MetricType =(
        (CPU, 'CPU Cores'),
        (RAM, 'RAM Used'),
    )

    collection = models.ForeignKey(Collection)
    org_name = models.CharField(max_length=50)
    vm_id = models.CharField(max_length=50)
    value = models.IntegerField()
    metric_type = models.CharField(max_length=3, choices=__MetricType)

    def __str__(self):
         return self.org_id

