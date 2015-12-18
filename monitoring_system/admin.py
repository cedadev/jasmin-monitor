from django.contrib import admin
from .models import Resource

class ChildAdmin(admin.ModelAdmin):
    pass

admin.site.register(Resource, ChildAdmin)