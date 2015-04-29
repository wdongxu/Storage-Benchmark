#!/usr/bin/python

import os
import sys
import subprocess

# Constants
vmstring="fio-driver-"
volstring="fio-driver-"
device_id = "/dev/vdc"

if os.environ.get('OS_AUTH_URL') and os.environ.get('OS_USERNAME') and os.environ.get('OS_PASSWORD') and os.environ.get('OS_TENANT_NAME') and os.environ.get('OS_TENANT_ID'):
	#Get FIO Servers
	server_id = subprocess.check_output("nova list | grep " + vmstring + "| grep Running | awk '{print $2}'", shell=True).split()

	#Get FIO Volumes
	volume_id = subprocess.check_output("nova volume-list | grep " + volstring + "| grep available | awk '{print $2}'", shell=True).split()

	# Servers and Volumes Tuple
	server_volume = zip(server_id, volume_id)

	for combo in server_volume:
		srv, vol = combo
		print("Executing: nova volume-attach " + srv + " " + vol + " " + device_id)
		subprocess.call(['nova', 'volume-attach', srv, vol, device_id])
else:
	print("Source the environment file for your target cloud")	
