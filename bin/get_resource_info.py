#!/home/njthykkathu/jasmine-venv/bin/python

"""
This module is executed in crontab. It creates a session in VCloud Directory.
gets the organisation id and using that retrieves the VApp id and checks if the
Vm is powered on in each VApp. If the Vm is powered on, it will get then take a
snapshot of amount of resources being used.
"""

__author__ = "Nijin Thykkathu"
__copyright__ = "Copyright 2015 UK Science and Technology Facilities Council"


import os
import sys
import django
from configparser import SafeConfigParser
from jasmin_portal.cloudservices.vcloud import VCloudProvider
import xml.etree.ElementTree as ET
import re
from django.core import serializers

parser = SafeConfigParser()
# change directory if needed
parser.read('/home/njthykkathu/jasmin_monitoring/config/r_config.ini')
path = parser.get('config', 'syspath')
username = parser.get('config', 'username')
password = parser.get('config', 'password')
print(username)

# Setting Django
sys.path.append(path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jasmin_monitoring.settings")
django.setup()
from monitoring_system.models import Resource, Collection

# Prefixes for vCD namespaces
_NS = {
    'vcd' : 'http://www.vmware.com/vcloud/v1.5',
    'ovf' : 'http://schemas.dmtf.org/ovf/envelope/1',
    'vmw' : 'http://www.vmware.com/schema/ovf',
    'rasd': 'http://schemas.dmtf.org/wbem/wscim/1/cim-schema/2/CIM_ResourceAllocationSettingData'
}

# Create a session
sess = VCloudProvider('https://vcloud.jasmin.ac.uk/api').new_session(username, password)

#----------------------------------------------------------------------------------------------------------------------#

# Getting Org ID from the org list
def GetOrg(sess):

    get_org = ET.fromstring(sess.api_request('GET', '/org').text)
    org_ref = get_org.findall('.//vcd:Org[@type="application/vnd.vmware.vcloud.org+xml"]', _NS)
    if org_ref is None:
        raise ProvisioningError('Unable to find organisation for user')
    for org_list in org_ref:
        org_id = ET.fromstring(sess.api_request('GET', org_list.attrib['href']).text)
        # Parsed the ID
        #parse_org_id = org_id.attrib['href'].rstrip('/').split('/').pop()
        org_name = org_id.attrib['name']
        return org_id, org_name


# Getting Vapp ID using the org id
def GetVapp(org_id):
    vdc_ref = org_id.find('.//vcd:Link[@type="application/vnd.vmware.vcloud.vdc+xml"]', _NS)
    if vdc_ref is None:
        raise ProvisioningError('Organisation has no VDCs')
    # Using the vdc find vapps
    get_vdc = ET.fromstring(sess.api_request('GET',vdc_ref.attrib['href']).text)
    vapp_ref = get_vdc.findall('.//vcd:ResourceEntity[@type="application/vnd.vmware.vcloud.vApp+xml"]', _NS)
    return vapp_ref


# Retrieves core data and adds to the database
def core_data(get_vm, org_name, vm_id, collection):
    core_ref = get_vm.find('.//vcd:Vm//vmw:CoresPerSocket', _NS).text
    # Adding data to database
    collection.resource_set.create(org_name=org_name, vm_id=vm_id, value=core_ref, metric_type=Resource.CPU)

# Retrieves core data and adds to the database
def core_data(get_vm, org_name, vm_id, collection):
    core_ref = get_vm.find('.//vcd:Vm//vmw:CoresPerSocket', _NS).text
    # Adding data to database
    collection.resource_set.create(org_name=org_name, vm_id=vm_id, value=core_ref, metric_type=Resource.RAM)

# Retrieves core data and adds to the database
def ram_data(status, org_name, vm_id, collection):
        vm_href = status.attrib['href']
        get_ram = ET.fromstring(sess.api_request('GET', vm_href + '/virtualHardwareSection/memory').text)
        ram_ref = get_ram.find('.//rasd:VirtualQuantity', _NS).text
        print(ram_ref)
        # Adding data to database
        collection.resource_set.create(org_name=org_name, vm_id=vm_id, value=ram_ref, metric_type=Resource.RAM)

#----------------------------------------------------------------------------------------------------------------------#

# Executes the program
get_org = GetOrg(sess)
get_vapp = GetVapp(get_org[0])

# the model is created here is because one time per snapshot of data
# if it was in the loop, each time would have created or each object created.
collection = Collection.objects.create()
collection.save()

# Getting VM ID and the resources information's
for vapp_list in get_vapp:
    get_vm = ET.fromstring(sess.api_request('GET', vapp_list.attrib['href']).text)
    status_ref = get_vm.find('.//vcd:Children', _NS)
    for status in status_ref:
        # Checks if the vm is powered on
        if status.attrib['status'] == '4':
            parse_vm_id = status.attrib['href'].rstrip('/').split('/').pop()
            core_data(get_vm, get_org[1], parse_vm_id, collection)
            ram_data(status, get_org[1], parse_vm_id, collection)
        else:
            pass

#----------------------------------------------------------------------------------------------------------------------#