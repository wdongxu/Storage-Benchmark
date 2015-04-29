#!/bin/bash

# This script take input file which defines the following information
# vms<list of VM IP>
# but the valuable info for installer.sh is only vms

# load config file
#conf=$1

#if [ ! -e $conf ]; then
#        echo "Configuration file $conf does not exit"
#        exit
#fi

#source ./$conf

function load
{
	for i in $vms; do
		echo $i
		echo "$fio_setup"
		case "$fio_setup" in
   			ssh) echo "enable ssh connection (copy ssh key and add server into trust list)"
				ssh-copy-id $i
                                eval $(ssh-agent)
                                ssh-add
    			;;
   			inst) echo "install ksh, fio and sysstat"
                                #sudo apt-get install ksh
                                ssh $i 'sudo apt-get install ksh'
                                #sudo apt-get install fio
                                ssh $i 'sudo apt-get install fio'
                                #sudo apt-get install sysstat
                                ssh $i 'sudo apt-get install sysstat'
			;;
   			fmat) echo "format and mount drive "$dr 
    			        ssh $i 'sudo cp /tmp/quick_vdbench_test /mnt/vdb/TEST/'
                                ssh $i 'sudo umount -l /mnt/vdb'
                                ssh $i 'sudo mkfs.ext4 /dev/'$dr
                                ssh $i 'sudo mkdir /mnt/'$dr
                                ssh $i 'sudo mount -t ext4 /dev/'$dr '/mnt/'$dr
                                ssh $i 'sudo chown ubuntu:ubuntu /mnt/'$dr
			;;
                        chk) 
				case "$fio_check" in
					drives) echo "check drives"
                        			ssh $i "df -h"
					;;
					connection) echo "check ssh connection"
                        			ssh $i "exit"
					;;
                        		test) echo "check fio on slaves"
                                		ssh $i "fio --version"
                        		;;
				esac
   			#*) #echo "Usage: $0 -r <osd|mon|rgw> -m <mon directory> -o <osd directory> -v <upgrade version for ceph>  "
    			#	usage
			#;;
		esac
	done
}

function usage
{
	echo "Usage: $0 -f *.config -r <ssh|inst|fmat|chk> -c <drives|connection|test> (opt;w/ chk only) -d <vdb|vdc|vde...> (opt;w/ fmat only) "
	exit 1
}


echo "===================start=================="
#load configuration file vms then install fio
numargs=$#
if [ ${numargs} -gt 6 ] || [ ${numargs} -lt 1 ]; then
    usage
fi

dr="vdb"

while getopts f:r:c:d:h:? opt; do
  case $opt in
    f)echo "-f is for input config file use: $OPTARG";
		fio_config=$OPTARG;
    ;;
    r)echo "-r is for exec setup fio use: $OPTARG";
		fio_setup=$OPTARG;
    ;;
    c)echo "-c is for check fio use: $OPTARG";
                fio_check=$OPTARG;
    ;;
    d)echo "-d is for assign format drive use: $OPTARG";
                dr=$OPTARG;
    ;;
    h)echo "help "
                usage
    ;;		
    ?)echo "help "
		usage
    ;;
  esac
done

# load config file
conf=$fio_config

if [ ! -e $conf ]; then
        echo "Configuration file $conf does not exit"
        exit
fi

source ./$conf

load
echo "===================done=================="
