from django.shortcuts import render

from django.http import HttpResponse

from .models import Resource
from django.template import RequestContext, loader
from django.shortcuts import render_to_response




# Create your views here.


def resource(request):
    total_query = Resource.objects.all()
    cpu_query = Resource.objects.filter(Metric_Type=Resource.CPU)
    ram_query = Resource.objects.filter(Metric_Type=Resource.RAM)
    template = loader.get_template('monitoring_system/main.html')
    context = RequestContext(request, {'total_data': total_query, 'cpu': cpu_query, 'ram': ram_query, })
    return HttpResponse(template.render(context))


# Alternative method

#def index(request):
 # return render_to_response('monitoring_system/main.html', {'obj': Resource.objects.all(), 'cpu': Resource.objects.filter(Metric_Type=Resource.CPU)})
