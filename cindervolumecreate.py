#!/usr/bin/python

import os
import sys
import subprocess

# Constants
vmstring="fio-driver-"
volstring="fio-driver-"
device_id = "/dev/vdb"
vol-type="ssd-high"
vol-size=80

start=input("please give a fio-drive-## start:")
end=input("please give a fio-drive-## end:")

if os.environ.get('OS_AUTH_URL') and os.environ.get('OS_USERNAME') and os.environ.get('OS_PASSWORD') and os.environ.get('OS_TENANT_NAME') and os.environ.get('OS_TENANT_ID'):
	#Get FIO Servers
	#server_id = subprocess.check_output("nova list | grep " + vmstring + "| grep Running | awk '{print $2}'", shell=True).split()

	#Get FIO Volumes
	#volume_id = subprocess.check_output("nova volume-list | grep " + volstring + "| awk '{print $2}'", shell=True).split()

	# Servers and Volumes Tuple
	#server_volume = zip(server_id, volume_id)

	#for combo in server_volume:
	for i in range(start,end+1):
		#srv, vol = combo
		volname='fio-driver-' + str(i)
		print("Executing: cinder create --display-name " + volname + " --volume-type " + vol-type + " " + vol-size)
		subprocess.call(['cinder', 'create', '--display-name', volname, '--volume-type', vol-type, vol-size])
else:
	print("Source the environment file for your target cloud")	
