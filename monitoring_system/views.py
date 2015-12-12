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
from django.db.models import Count
from django.db import connection
from django.core.serializers.json import DjangoJSONEncoder


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
def cpu_period(request, format=None):
    if request.method == 'GET':
        metric_type = request.GET.get('metric_type', '')
        start = request.GET.get('start', '')
        if not metric_type:
            metric_type = 'CPU'
        if not start:
            last_year = datetime.datetime.now() - datetime.timedelta(days=1*365)
            start = datetime.date.strftime(last_year, "%Y-%m-%d") # default start date
        end = request.GET.get('end', '')
        if not end:
            now = datetime.datetime.now()
            end = datetime.date.strftime(now, "%Y-%m-%d %H:%M:%S") # default end date
        cursor = connection.cursor()
        print(metric_type)
        cursor.execute("SELECT collection_time, SUM(value) FROM monitoring_system_collection, \
         monitoring_system_resource WHERE monitoring_system_collection.id = collection_id AND metric_type = %s \
         AND collection_time BETWEEN %s AND %s \
         GROUP BY collection_time ORDER BY collection_time", (metric_type, start, end))
        response = []
        for query_data in cursor:
            per_collection = datetime.date.strftime(query_data[0], "%Y-%m-%d %H:%M:%S") # default start date
            value = query_data[1]

            response.append({'collection_time':per_collection,'total':value})
        to_json = json.dumps(response)
        return Response(response)


########################################################################################################################


# Use this for the aggregation of months, week and year and also for day
# SELECT date_trunc('day', collection_time) AS day, AVG(total)
# FROM (
#     SELECT collection_time, SUM(value) AS total
#     FROM monitoring_system_collection AS c, monitoring_system_resource AS r
#     WHERE c.id = r.collection_id AND r.metric_type = 'CPU' AND c.collection_time BETWEEN '2015-11-01 00:00:00' AND '2015-12-04 00:00:00'
#     GROUP BY collection_time ORDER BY collection_time
# ) AS totals
# GROUP BY day ORDER BY day


@api_view(['GET'])
def per_day(request, format=None):
    if request.method == 'GET':
        metric_type = request.GET.get('metric_type', '')
        start = request.GET.get('start', '')
        end = request.GET.get('end', '')
        cursor = connection.cursor()
        if not start:
            last_year = datetime.datetime.now() - datetime.timedelta(days=1*365)
            start = datetime.date.strftime(last_year, "%Y-%m-%d") # default start date
        else:
            start = start
        if not end:
            now = datetime.datetime.now()
            end = datetime.date.strftime(now, "%Y-%m-%d %H:%M:%S") # default end date
        else:
            end = end
        cursor.execute("SELECT date_trunc('day', monitoring_system_collection.collection_time),count (*) \
        FROM monitoring_system_collection WHERE collection_time BETWEEN %s AND %s GROUP BY date_trunc('day', \
        collection_time) ORDER BY date_trunc('day', collection_time)", (start, end))
        response = []
        for query_data in cursor:
            per_day = datetime.date.strftime(query_data[0], "%Y-%m-%d") # default start date
            print(per_day)
            total_collection = query_data[1]
            response.append({'day':per_day,'value':total_collection})
        to_json = json.dumps(response)
        print(response)
        return Response(response)


########################################################################################################################

# Need to sort out the error coming from the javascript
@api_view(['GET'])
def per_week(request, format=None):
    if request.method == 'GET':
        metric_type = request.GET.get('metric_type', '')
        start = request.GET.get('start', '')
        end = request.GET.get('end', '')
        cursor = connection.cursor()
        if not start:
            last_year = datetime.datetime.now() - datetime.timedelta(days=1*365)
            start = datetime.date.strftime(last_year, "%Y-%m-%d") # default start date
        else:
            start = start
        if not end:
            now = datetime.datetime.now()
            end = datetime.date.strftime(now, "%Y-%m-%d %H:%M:%S") # default end date
        else:
            end = end
        cursor.execute("SELECT date_trunc('week', collection_time) AS week, AVG(total) FROM ( \
    SELECT collection_time, SUM(value) AS total\
    FROM monitoring_system_collection AS c, monitoring_system_resource AS r\
    WHERE c.id = r.collection_id AND r.metric_type = %s AND c.collection_time BETWEEN %s AND %s\
    GROUP BY collection_time ORDER BY collection_time) AS totals GROUP BY week ORDER BY week", (metric_type, start, end))
        response = []
        for query_data in cursor:
             #print(query_data)
             per_week = datetime.date.strftime(query_data[0], "%Y-%m-%d") # default start date
             print(per_week)
             avg_used = query_data[1]
             print(str(avg_used))
             response.append({'week':per_week,'value':str(avg_used)})
        #to_json = json.dumps(response)
        return Response(response)


########################################################################################################################

# Need to sort out the error coming from the javascript
@api_view(['GET'])
def per_month(request, format=None):
    if request.method == 'GET':
        metric_type = request.GET.get('metric_type', '')
        start = request.GET.get('start', '')
        end = request.GET.get('end', '')
        cursor = connection.cursor()
        if not start:
            last_year = datetime.datetime.now() - datetime.timedelta(days=1*365)
            start = datetime.date.strftime(last_year, "%Y-%m-%d") # default start date
        else:
            start = start
        if not end:
            now = datetime.datetime.now()
            end = datetime.date.strftime(now, "%Y-%m-%d %H:%M:%S") # default end date
        else:
            end = end
        cursor.execute("SELECT date_trunc('month', collection_time) AS month, AVG(total) FROM ( \
    SELECT collection_time, SUM(value) AS total\
    FROM monitoring_system_collection AS c, monitoring_system_resource AS r\
    WHERE c.id = r.collection_id AND r.metric_type = %s AND c.collection_time BETWEEN %s AND %s\
    GROUP BY collection_time ORDER BY collection_time) AS totals GROUP BY month ORDER BY month", (metric_type, start, end))
        response = []
        for query_data in cursor:
             #print(query_data)
             per_month = datetime.date.strftime(query_data[0], "%Y-%m-%d") # default start date
             #print(per_week)
             avg_used = query_data[1]
             #print(str(avg_used))
             response.append({'month':per_month,'value':str(avg_used)})
        #to_json = json.dumps(response)
        return Response(response)

# ########################################################################################################################
#
#
# @api_view(['GET'])
# def per_year(request, format=None):
#     if request.method == 'GET':
#         metric_type = request.GET.get('metric_type', '')
#         start = request.GET.get('start', '')
#         end = request.GET.get('end', '')
#         cursor = connection.cursor()
#         if not start:
#             last_year = datetime.datetime.now() - datetime.timedelta(days=1*365)
#             start = datetime.date.strftime(last_year, "%Y-%m-%d") # default start date
#         else:
#             start = start
#         if not end:
#             now = datetime.datetime.now()
#             end = datetime.date.strftime(now, "%Y-%m-%d %H:%M:%S") # default end date
#         else:
#             end = end
#         cursor.execute("SELECT date_trunc('year', monitoring_system_collection.collection_time),count (*) \
#         FROM monitoring_system_collection WHERE collection_time BETWEEN %s AND %s GROUP BY date_trunc('day', \
#         collection_time) ORDER BY date_trunc('day', collection_time)", (start, end))
#         response = []
#         for query_data in cursor:
#             per_day = datetime.date.strftime(query_data[0], "%Y-%m-%d") # default start date
#             print(per_day)
#             total_collection = query_data[1]
#             response.append({'day':per_day,'value':total_collection})
#         to_json = json.dumps(response)
#         return Response(response)
#
#
# ########################################################################################################################








     #   file = json.dumps({'numbers':value, 'strings':start})


     #   hello = json.dumps([dict(total=pn) for pn in start])
     #   return Response(hello)
#

     #   print(file)


    #     for
    #     response = {'count': count, 'year' : year}
    #     jsondata = json.dumps(response)
    # return HttpResponse(jsondata)


        # if request.method == 'GET':
        #     collections = Collection.objects
        #     start = request.GET.get('start', '')
        #     end = request.GET.get('end', '')
        #     if not start:
        #         last_year = datetime.datetime.now() - datetime.timedelta(days=1*365)
        #         start = datetime.date.strftime(last_year, "%Y-%m-%d") # default start date
        #     else:
        #         start = datetime.datetime.strptime(start, "%Y-%m-%d")
        #     collections = collections.filter(collection_time__gte = start)
        #     if not end:
        #         now = datetime.datetime.now()
        #         end = datetime.date.strftime(now, "%Y-%m-%d %H:%M:%S") # default end date
        #     else:
        #         end = datetime.datetime.strptime(end, "%Y-%m-%d")
        #     collections = collections.filter(collection_time__lte = end)
        #     serializer = PerDay(collections, many=True)
        #     return Response(serializer.data)

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
