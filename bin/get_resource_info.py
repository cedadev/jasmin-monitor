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

# Prefixes for vCD namespaces
_NS = {
    'vcd' : 'http://www.vmware.com/vcloud/v1.5',
    'ovf' : 'http://schemas.dmtf.org/ovf/envelope/1',
    'vmw' : 'http://www.vmware.com/schema/ovf',
}

# Retrieving info from VCloud directory
# Create a session
sess = VCloudProvider('https://vcloud.jasmin.ac.uk/api').new_session(username,password)

# Getting Org id from the org list
results1 = ET.fromstring(sess.api_request('GET', '/org').text)
org_ref = results1.findall('.//vcd:Org[@type="application/vnd.vmware.vcloud.org+xml"]', _NS)
#org_ids = [app.attrib['href'].rstrip('/').split('/').pop() for app in results1]

for org_list in org_ref:
    org = ET.fromstring(sess.api_request('GET', org_list.attrib['href']).text)
    # Then get the VDC from the org
    vdc_ref = org.find('.//vcd:Link[@type="application/vnd.vmware.vcloud.vdc+xml"]', _NS)
 #   print(vdc_ref)
    if vdc_ref is None:
        raise ProvisioningError('Organisation has no VDCs')
  #  print(vdc_ref.attrib['href'])
    #vdc_id = vdc_ref.attrib['href'].rstrip('/').split('/').pop()
   # print(vdc_id)

    # Using the vdc find vapps
    results = ET.fromstring(sess.api_request('GET',vdc_ref.attrib['href']).text)
    vapps = results.findall('.//vcd:ResourceEntity[@type="application/vnd.vmware.vcloud.vApp+xml"]', _NS)


    for vapp_list in vapps:
        print(vapp_list.attrib['href'])
        vm_ref = ET.fromstring(sess.api_request('GET', vapp_list.attrib['href']).text)
        ip_range = vm_ref.find('.//vcd:Children', _NS)


        # Got the Vapp, now need to find the status and core of each Vapp

        # Need to go to vcloud directory and check each vms cores
        # Need to add power on before

        # Seems that the code below is showing the core, need to re-confirm it
        core = vm_ref.find('.//vcd:Vm//vmw:CoresPerSocket', _NS).text
        print(core)
        #vms = ip_range.find('./vcd:Vm[@status="4"]', _NS)


        # for vm_list in vms:
        #     print(vm_list.attrib["href"])
        # if the vapp











# #GET /org/{id}
#
# # Using the org list find vapps
# results = ET.fromstring(sess.api_request('GET', 'vApps/query').text)
# apps = results.findall('vcd:VAppRecord', _NS)
# machine_ids = [app.attrib['href'].rstrip('/').split('/').pop() for app in apps]
#
# for id_list in machine_ids:
#     print(id_list)










#org_list = sess.api_request('GET', '/org').text

# results = ET.fromstring(sess.api_request('GET', '/org').text)
# print(results)
#xmldata = ET.fromstring(org_list)

# for id_list in xmldata:
#     list = id_list.attrib
#     print(list)



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