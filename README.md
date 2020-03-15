CPU and memory metric of Linux system. Test task.

# Description

CLI tool to print CPU and Memory Utilization.

## Usage:
```
    $ ./metrics.py [cpu|mem]
```

### Requirements:

*python3
*pip3 
*psutil

## Installation:
```
git clone <https://github.com/OleksPo/metric-for-fedora.git>
sudo yum install gcc python3-devel
sudo pip3 install psutil --user
```

## Sample output:
```
`$ ./metrics.py cpu`

system.cpu. user         1.2

system.cpu. nice         0.0

system.cpu. system       0.2

system.cpu. idle         98.0

system.cpu. iowait       0.0

system.cpu. irq          0.2

system.cpu. softirq      0.2

system.cpu. steal        0.0

system.cpu. guest        0.0

system.cpu. guest_nice   0.0
```

```
`$ ./metrics.py mem`

virtual total   4111085568

virtual available   711323648

virtual percent   82.7

virtual used   2995433472

virtual free   171413504

virtual active   2604814336

virtual inactive   941674496

virtual buffers   45191168

virtual cached   899047424

virtual shared   172609536

virtual slab   205680640

swap  total      4269797376

swap  used       201064448

swap  free       4068732928

swap  percent    4.7

swap  sin        2060288

swap  sout       201388032
```

### Docker
