from django.shortcuts import render
from .models import Resource
from django.http import HttpResponse
#from monitoring_system.serializers import ResourceSerializer
from monitoring_system.serializers import PerDay
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers
from .models import Collection
import json
import datetime

#
# # Create your views here.
#
# def resource(request):
#     total_query = Resource.objects.all()
#     cpu_query = Resource.objects.filter(Metric_Type=Resource.CPU)
#     ram_query = Resource.objects.filter(Metric_Type=Resource.RAM)
#     template = loader.get_template('monitoring_system/checking.html')
#     context = RequestContext(request, {'total_data': total_query, 'cpu': cpu_query, 'ram': ram_query, })
#     return HttpResponse(template.render(context))
#
# def cpu(request):
#     cpu_query = Resource.objects.filter(Metric_Type=Resource.CPU)
#     template = loader.get_template('monitoring_system/cpu.html')
#     context = RequestContext(request, {'cpu': cpu_query})
#     return HttpResponse(template.render(context))
#
# def ram(request):
#     ram_query = Resource.objects.filter(Metric_Type=Resource.RAM)
#     template = loader.get_template('monitoring_system/ram.html')
#     context =

@api_view(['GET'])
def resource_list(request, format = None):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        total_resource = Resource.objects.all()
        serializer = ResourceSerializer(total_resource, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def cpu_day_list(request, format = None):

    if request.method == 'GET':
       query = Collection.objects.all()
       collection = []
       for total in query:
           collection.append(total.total(Resource.CPU))
       serializer = PerDay(query, many=True)
       return Response(serializer.data)


@api_view(['GET'])
def cpu_day_detail(request, format = None):
        if request.method == 'GET':
           query = Collection.objects.all()
           collection = []
           # for total in query:
           #     collection.append(total.total(Resource.CPU))
           serializer = PerDay(query, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def cpu_period(request, format = None):
        if request.method == 'GET':
            start = datetime.date(2015,11,18)
            end = datetime.date(2015,11,19)
            period = Collection.objects.filter(collection_time__range=[start,end])
            serializer = PerDay(period, many=True)
        return Response(serializer.data)

########################################################################################################################

@api_view(['GET'])
def cpu_period(request, format = None):
        if request.method == 'GET':
            collections = Collection.objects
            if 'start' in request.GET:
                if request.GET['start'] == '':
                    last_year = datetime.datetime.now() - datetime.timedelta(days=1*365)
                    def_start = datetime.date.strftime(last_year, "%Y-%m-%d") # default start date
                    collections = collections.filter(collection_time__gte = def_start)
                else:
                    start = datetime.datetime.strptime(request.GET['start'], "%Y-%m-%d")
                    collections = collections.filter(collection_time__gte = start)
            if 'end' in request.GET:
                if request.GET['end'] == '':
                    now = datetime.datetime.now()
                    def_end = datetime.date.strftime(now, "%Y-%m-%d") # default end date
                    collections = collections.filter(collection_time__lte = def_end)
                else:
                    end = datetime.datetime.strptime(request.GET['end'], "%Y-%m-%d")
                    collections = collections.filter(collection_time__lte = end)
            serializer = PerDay(collections, many=True)
            return Response(serializer.data)

########################################################################################################################



       #  check = json.dumps(collection)
       #
       # # hello = json.dumps([dict(total=pn) for pn in collection])
       #  return Response(check)




       #serializer = AlbumSerializer(instance=query)
       #next = AlbumSerializer(query, many=True)
       #return Response(serializer.data)
        # looks like this works, but not returning a list, maybe try and get it going
        #
        #
        #   #cpu_query = Resource.objects.filter(metric_type=Resource.CPU)
       # collection = Collection.objects.all()[0].total(Resource.CPU)




     #   value = [v.value for v in cpu_query]


        # Mean Calculation - Need into function maybe
        # results = list(map(int, value))
        # length = len(results)
        #
        #
        # for i in range(length):
        #     total_sum = results[i]
        # total_sum = sum(results)
        #
        # average = total_sum/length

     #   date = [v.date_time for v in cpu_query]

       # serializer = PerDay(cpu_query, many=True)


















# Need to come back to this
# def login_view(request):
#     state = "Please login below..."
#     username = password = ''
#     if request.POST:
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 state = "You're successfully logged in!"
#             else:
#                 state = "Your account is not active, please contact the site admin."
#         else:
#             state = "Your username and/or password were incorrect."
#
#     return render_to_response('login.html',{'state':state, 'username': username})

# def resource(request):
#     table = ResourceTable(Resource.objects.all())
#     RequestConfig(request).configure(table)
#     return render(request, 'monitoring_system/main.html', {'table': table})
# Alternative method

#def index(request):
 # return render_to_response('monitoring_system/main.html', {'obj': Resource.objects.all(), 'cpu': Resource.objects.filter(Metric_Type=Resource.CPU)})
