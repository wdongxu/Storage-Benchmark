#!/usr/bin/python

import os
import sys
import subprocess

# Constants
vmstring="fio-driver-"
volstring="fio-driver-"

VM_NAMEstring="fio-driver-"

start=input("please give a fio-drive-## start:")
end=input("please give a fio-drive-## end:")


if os.environ.get('OS_AUTH_URL') and os.environ.get('OS_USERNAME') and os.environ.get('OS_PASSWORD') and os.environ.get('OS_TENANT_NAME') and os.environ.get('OS_TENANT_ID'):
	#for nova boot from image with flavor and nic cards:
	for i in range(start,end+1):
		#srv, vol = combo
		VM_NAME=VM_NAMEstring + str(i)
		print("Executing: nova delete " + VM_NAME)
		subprocess.call(['nova', 'delete', VM_NAME])
else:
	print("Source the environment file for your target cloud")	
