#!/home/njthykkathu/jasmine-venv/bin/python

import django
import os
import sys
import string
from configparser import SafeConfigParser


parser = SafeConfigParser()
parser.read('/home/njthykkathu/jasmin_monitoring/config/r_config.ini')
path = parser.get('config', 'syspath')
# Setting Django
sys.path.append(path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jasmin_monitoring.settings")
django.setup()

from django.shortcuts import render
from django.utils import timezone
from monitoring_system.models import Resource
from monitoring_system.models import Collection
import datetime
import random


past = timezone.now() - datetime.timedelta(days=730)
while (past <= timezone.now()):
    collection=Collection.objects.create(collection_time=past)
    collection.save()
    org_names = random.randrange(1, 2, 1)
    while(org_names <=2):
        chars=string.ascii_lowercase
        first_word = "First"
        second_word = "Second"
        num = "123"
        if org_names == 1:
            org_name = first_word+num
        else:
            org_name = second_word+num
        #org_id = word+str(num)
        count =random.randrange(1, 3, 1)
        while(count < 3):
            collection_time = past
            chars=string.ascii_lowercase
            w = ''.join(random.choice(chars) for i in range(3))
            n = random.randrange(100, 1000, 3)
            vm_id = w+str(n)
            value = random.randrange(1, 4, 1)
            metric = random.randrange(1, 2, 1)
            while(metric <= 2):
                if metric == 1:
                    metric_type = 'CPU'
                    print (org_name, vm_id, value, metric_type,past)
                    collection.resource_set.create(org_name=org_name,vm_id=vm_id,value=value,metric_type=Resource.CPU)
                else:
                    metric_type = 'RAM'
                    ram = random.randrange(1, 4, 1)
                    if ram == 1:
                        value = "1024"
                    elif ram == 2:
                        value = "2048"
                    else:
                        value = "512"
                    print (org_name, vm_id, value, metric_type,past)
                    collection.resource_set.create(org_name=org_name,vm_id=vm_id,value=value,metric_type=Resource.RAM)
                metric = metric + 1
            count = count + 1
        print("Done Here")
        org_names = org_names + 1
    past = past + datetime.timedelta(minutes=10)


print("Good bye!")


