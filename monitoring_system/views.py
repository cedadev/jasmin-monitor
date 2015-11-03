from django.shortcuts import render

from django.http import HttpResponse

from .models import Resource


# Create your views here.


def index(request):
    table = Resource.objects.all()
    return HttpResponse(table)

