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
2. You need to have proper priviledge for create VMs, volumes ...etc
3. You need to have enough storage space for benchmarking test.
```

#### Environment Setup - Openstack Nova VMs, Cinder Volumes and Mount Cinder Volumes to Nova VMs 
```bash
1 Nova boot controller with two nic cards
2 Nova boot slaves with one private nic card
3 create cinder volumes
4 mount cinder volumes
```
#### fio Setup - mount the drives on 
```bash
1.copy ssh keys to make sure controller can reach all the slaves
2 install fio ( if guest OS ubuntu doesn't need it )
3 format and mount the testing drives
4 trigger fio testing load from controller
```
#### vdbench Setup - mount the drives on 
```bash
1.copy ssh keys to make sure controller can reach all the slaves
2 install vdbench
3 format and mount the testing drives
4 trigger fio testing load from controller
```

#### Clean Environment - Openstack Nova VMs, Cinder Volumes and Mount Cinder Volumes to Nova VMs 
```bash
1 detach cinder voumes
2 delete nova vms
```


