import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class CommonData(models.Model):
    Org_ID = models.CharField(max_length=50)
    Vm_ID = models.CharField(max_length=50)
    Value = models.CharField(max_length=5)
    Date_Time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.Org_ID

    class Meta:
        abstract = True


class Resource(CommonData):
    metric_list = (
        ('CPU', 'CPU Cores'),
        #('RAM', 'RAM'),
    )
    Metric_Type = models.CharField(max_length=3, choices=metric_list)