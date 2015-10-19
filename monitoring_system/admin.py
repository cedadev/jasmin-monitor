from django.contrib import admin

from .models import Metric, Vapp, Vm_core

# Register your models here.

admin.site.register(Metric)

admin.site.register(Vapp)

admin.site.register(Vm_core)

#admin.site.register(Vm_ram)