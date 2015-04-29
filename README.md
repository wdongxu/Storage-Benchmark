# Storage-Benchmark
This project is providing storage benchmark tools ; fio and vdbench on Openstack plantform.

## It is Python and Bash Shell Script
### It is not Eclipse IDE project and have to base on openstack environment
####fio and vdbench automation for Storage Performance Benchmarking.

All the detail can be found in my [blog](http://chianingwang.blogspot.com/2015/01/minhash-for-file-similarity.html)

#### Hint
```bash
Here are the items for the hint.
1. You need to have openstack environment for testing
2. You need to have proper privilege for create VMs, volumes ...etc
3. You need to have enough storage space (HDD/SSD) for benchmarking test
4. You need to know IPs for controller and slaves ( static or float IPs )
```

#### Environment Setup - Nova VMs, Cinder Vols and Mount Vols 
```bash
1 Nova boot controller with two nic cards
  #vim ./novavmcreate.py 
  enable nic_id1string="public nic_id"
  enable nova boot with two nic_ids
  remark nova boot with one nic_ids
  #./novavmcreate.py
  give the seq no for start VM eg: 1
  give the seq no for last VM eg: 1
2 Nova boot slaves with one private nic card
  #vim ./novavmcreate.py 
  remark nic_id1string="public nic_id"
  enable nova boot with one nic_ids
  remark nova boot with two nic_ids
  #./novavmcreate.py
  give the seq no for start VM eg: 2 
  give the seq no for last VM eg: 160
3 create cinder vols
  #./cindervolumecreate.py
  give the seq no for start vol eg: 1
  give the seq no for last vol eg: 160
4 mount cinder vols
  # ./novavolumeattach.py
  give the mount drive name eg: vdb or vdc ... etc

```

#### fio Setup - mount the drives on 
```bash
1 prepare vm.conf which includes all the slave's IPs eg: vm.conf
2 ssh controller
  #ssh-keygen
3 copy ssh keys to make sure controller can reach all the slaves
  #./fio_install.sh -f vm.conf -r ssh
4 install fio ( if guest OS ubuntu doesn't need it )
  #./fio_install.sh -f vm.conf -r inst
5 format and mount the testing drives
  #./fio_install.sh -f vm.conf -r fmat -d vdb
6 trigger fio testing load from controller
  #fio job_file
  PS: Job file format
  -------------------
  ; -- start job file --
  [random-writers]
  ioengine=libaio
  iodepth=4
  rw=randwrite
  bs=32k
  direct=0
  size=64m
  numjobs=4
  ; -- end job file --
  -------------------
  same with command
  #fio --name=global --rw=randread --size=128m --name=job1 --name=job2
```

#### vdbench Setup - mount the drives on 
```bash
1 prepare vm.conf which includes all the slave's IPs eg: vm.conf
2 ssh controller
  #ssh-keygen
3 copy ssh keys to make sure controller can reach all the slaves
  #./vdbench_install.sh -f vm.conf -r ssh
4 install fio ( if guest OS ubuntu doesn't need it )
  #./vdbench_install.sh -f vm.conf -r inst
5 format and mount the testing drives
  #./vdbench_install.sh -f vm.conf -r fmat -d vdb
6 enable vdbench rsh daemon on each slaves
  #./vdbench_install.sh -f vm.conf -r rsh
7 trigger vdbench testing load from controller
  #./vdbench -f parmfile
```

#### Clean Environment - Openstack Nova VMs, Cinder Volumes and Mount Cinder Volumes to Nova VMs 
```bash
1 detach cinder voumes
  #novavolumedetach.py
2 delete nova vms
  #novavmdelete.py
  give the seq no for start VM eg: 1
  give the seq no for last VM eg: 160
  
```
#### PS Extra-Utility for fio  
```bash
1 run df -h on all the slaves
  #./fio_install.sh -f vm.conf -r chk -c drive
2 test ssh connection on all the slaves
  #./fio_install.sh -f vm.conf -r chk -c connection
3 run fio --version , testing on all the slaves has fio or not
  #./fio_install.sh -f vm.conf -r chk -c test
```

#### PS Extra-Utility for vdbench  
```bash
1 run df -h on all the slaves
  #./vdbench_install.sh -f vm.conf -r chk -c drive
2 test ssh connection on all the slaves
  #./vdbench_install.sh -f vm.conf -r chk -c connection
3 run vdbench -t , testing on all the slaves w/o parmfile
  #./vdbench_install.sh -f vm.conf -r chk -c test
```

Any suggestion or comment will be welcome
