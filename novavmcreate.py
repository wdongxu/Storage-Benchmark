#!/usr/bin/python

import os
import sys
import subprocess

# Constants
vmstring="fio-driver-"
volstring="fio-driver-"

#nova image-list
imagestring="trusty-server-cloudimg-amd64-disk"

#nova flavor-list
flavorstring="m1.small"

#controller has 2 nic, public and private
#slaves has only 1 nic, private
#neutron net-list
#public-direct-604 = xxxxxxxxxa-xxxx-xxxx-xxxx-xxxxxxxxxxx
#nic_id1string="xxxxxxxxxa-xxxx-xxxx-xxxx-xxxxxxxxxxxe"
#private-net-3006 = xxxxxxxxxa-xxxx-xxxx-xxxx-xxxxxxxxxxx
nic_id2string="xxxxxxxxxa-xxxx-xxxx-xxxx-xxxxxxxxxxx"

VM_NAMEstring="fio-driver-"

start=input("please give a fio-drive-## start:")
end=input("please give a fio-drive-## end:")


if os.environ.get('OS_AUTH_URL') and os.environ.get('OS_USERNAME') and os.environ.get('OS_PASSWORD') and os.environ.get('OS_TENANT_NAME') and os.environ.get('OS_TENANT_ID'):
	#for nova boot from image with flavor and nic cards:
	for i in range(start,end+1):
		#srv, vol = combo
		VM_NAME=VM_NAMEstring + str(i)
		#print("Executing: nova boot --image " + imagestring + " --flavor " + flavorstring + " --nic net-id=" + nic_id1string + " --nic net-id=" + nic_id2string + " " + VM_NAME)
		#subprocess.call(['nova', 'boot', '--image', imagestring, '--flavor', flavorstring, '--nic', 'net-id=' + nic_id1string, '--nic', 'net-id=' + nic_id2string, VM_NAME])
		print("Executing: nova boot --image " + imagestring + " --flavor " + flavorstring + " --nic net-id=" + nic_id2string + " " + VM_NAME)
                subprocess.call(['nova', 'boot', '--image', imagestring, '--flavor', flavorstring, '--nic', 'net-id=' + nic_id2string, VM_NAME])
else:
	print("Source the environment file for your target cloud")	
