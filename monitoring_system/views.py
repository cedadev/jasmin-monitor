from django.shortcuts import render
from .models import Resource, Collection
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import datetime
from django.db.models import Count
from django.db import connection
from django.core.serializers.json import DjangoJSONEncoder

########################################################################################################################

@api_view(['GET'])
def main(request, format=None):
    if request.method == 'GET':
        org_name = request.GET.get('org_name', '')
        metric_type = request.GET.get('metric_type', '')
        time_period = request.GET.get('time_period', '')
        start = request.GET.get('start', '')
        if not time_period:
            time_period = 'Hour'
        if not metric_type:
            metric_type = 'CPU'
        if not start:
            last_year = datetime.datetime.now() - datetime.timedelta(days=1*365)
            start = datetime.date.strftime(last_year, "%Y-%m-%d ") # default start date
        end = request.GET.get('end', '')
        if not end:
            now = datetime.datetime.now()
            end = datetime.date.strftime(now, "%Y-%m-%d %H:%M:%S") # default end date
        cursor = connection.cursor()
        if not org_name:
            cursor.execute("SELECT date_trunc(%s, collection_time) AS date_time, AVG(total) FROM ( \
            SELECT collection_time, SUM(value) AS total FROM monitoring_system_collection AS c, \
            monitoring_system_resource AS r WHERE c.id = r.collection_id AND r.metric_type = %s \
            AND c.collection_time BETWEEN %s AND %s GROUP BY collection_time ORDER BY collection_time) \
            AS totals GROUP BY date_time ORDER BY date_time", (time_period, metric_type, start, end))
        else:
            cursor.execute("SELECT date_trunc(%s, collection_time) AS date_time, AVG(total) FROM ( \
            SELECT collection_time, SUM(value) AS total FROM monitoring_system_collection AS c, \
            monitoring_system_resource AS r WHERE r.org_name = %s AND c.id = r.collection_id AND r.metric_type = %s \
            AND c.collection_time BETWEEN %s AND %s GROUP BY collection_time ORDER BY collection_time) \
            AS totals GROUP BY date_time ORDER BY date_time", (time_period, org_name, metric_type, start, end))
        response = []
        for query_data in cursor:
            date_time = datetime.date.strftime(query_data[0], "%Y-%m-%d %H:%M:%S") # default start date
            avg_used = query_data[1]
            response.append({'datetime': date_time, 'value': str(avg_used)})
        return Response(response)


########################################################################################################################
