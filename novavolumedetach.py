#!/usr/bin/python

import os
import sys
import subprocess

# Constants
vmstring="fio-driver-"
volstring="fio-driver-"
device_id = "/dev/vdb"

if os.environ.get('OS_AUTH_URL') and os.environ.get('OS_USERNAME') and os.environ.get('OS_PASSWORD') and os.environ.get('OS_TENANT_NAME') and os.environ.get('OS_TENANT_ID'):
	#Get FIO Servers
	server_id  = subprocess.check_output("nova volume-list | grep "+ vmstring + "| grep in-use | awk '{print $12}'", shell=True).split()

	#Get FIO Volumes
	volume_id  = subprocess.check_output("nova volume-list | grep " + volstring + "| grep in-use | awk '{print $2}'", shell=True).split()

	# Servers and Volumes Tuple
	server_volume = zip(server_id, volume_id)

	for combo in server_volume:
		srv, vol = combo
		subprocess.call(['nova', 'volume-detach', srv, vol])
else:
	print("Source the environment file for your target cloud")
