#!/home/njthykkathu/jasmine-venv/bin/python

"""
This module ......



"""

__author__ = "Nijin Thykkathu"
__copyright__ = "Copyright 2015 UK Science and Technology Facilities Council"


import os
import sys
import django
from configparser import SafeConfigParser
from jasmin_portal.cloudservices.vcloud import VCloudProvider
#from xml.dom.minidom import parseString
import xml.etree.ElementTree as ET
import re

parser = SafeConfigParser()
parser.read('/home/njthykkathu/jasmin_monitoring/config/r_config.ini')
path = parser.get('config', 'syspath')
username = parser.get('config', 'username')
password = parser.get('config', 'password')

# Setting Django
sys.path.append(path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jasmin_monitoring.settings")
django.setup()
from monitoring_system.models import Resource

# Retrieving info from VCloud directory
# Create a session
sess = VCloudProvider('https://vcloud.jasmin.ac.uk/api').new_session(username,password)

# Getting Org id from the org list
org_list = sess.api_request('GET', '/org').text
xmldata = ET.fromstring(org_list)
for id_list in xmldata:
    list = id_list.attrib
    print(list)

# Using the org list find vapps


# Using the vapp list find the vm

# Using the vm list find the cpu cores used by each system



#-----------------------------------------------------------------------------------------------------------#

# dom = parseString(org_list)
# xmlTag = dom.getElementsByTagName('OrgList')[0].toxml()
# print (xmlTag)


# View the XML from an API request
#print(sess.api_request('GET', 'vApps/query').text)


# Getting the Org list
#print("ORG List")
#print(sess.api_request('GET', '/org').text)

# Get an Org
#print("ORG ID")
#print(sess.api_request('GET', '/org/1d28705f-b5ac-48d2-8bfc-308f407bd114').text)

#print("APP List from ORG")
# Gets all the Vapp in the Org - use the vdc from the org get list
#print(sess.api_request('GET', '/vdc/03d03a29-3c4c-490a-8cd2-164760e91db5').text)


# Get Details of particualar Vapp Id
#print(sess.api_request('GET', '/vApp/vapp-2331c443-39aa-4bf4-9940-627d0e745792').text)


# Adding data to database
# add_org = Metric.objects.create(org='thefinalorg')
# add_vapp = Vapp.objects.create(Vapp='thefinalapp', metric_id = 8)
#add_cm = Vm_core.objects.create(n_cores='10',Vapp_id=6)


# # Quering data from the Django database
#
# # for all the data
# #print(Vm_core.objects.all())
# # FOr month
# print(Vm_core.objects.filter(created_at__month=10))
# # for year
# print(Vm_core.objects.filter(created_at__month=2015))
#
#
# # Retrieves all the vm core related to vapp id 6
# e = Vapp.objects.get(id=6)
# print(e.vm_core_set.all())
#
# # Retrieves all the v app associated with the org
# a = Metric.objects.get(id=8)
# print(a.vapp_set.all())
