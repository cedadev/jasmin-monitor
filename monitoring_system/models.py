import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Metric(models.Model):
    org = models.CharField(max_length=50)

    def __str__(self):
        return self.org


class Vapp(models.Model):
    Vapp = models.CharField(max_length=50)
    metric = models.ForeignKey('Metric')

    def __str__(self):
        return self.Vapp


class Vm_core(models.Model):
    Vapp = models.ForeignKey('Vapp')
    n_cores = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.n_cores


# Adding Vm Ram
# class Vm_ram(models.Model):
#     Vapp = models.ForeignKey('Vapp')
#     n_ram = models.CharField(max_length=2)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.n_ram



# Different Design MOdel

# # the main table which contains the organisation and ids
# class Metric(models.Model):
#     org = models.CharField(max_length=30)
#     Vapp = models.CharField(max_length= 30)
#     Vm = models.CharField(max_length= 30)
#
#     def __str__(self):
#         return self.org
#
# class cpu(models.Model):
#     metric = models.ForeignKey('Metric')
#     created_at = models.DateTimeField(auto_now_add=True)
#     #timestamp = models.DateTimeField('date published')
#     n_cores = models.CharField(max_length=2)
#
#     def __str__(self):
#         return self.num_cores

#
# class ram(models.Model):
#     metric = models.ForeignKey('Metric')
#     timestamp = models.DateTimeField('date published')
#     ram = models.CharField(max_length=2)
#
#     def __str__(self):
#         return self.ram
