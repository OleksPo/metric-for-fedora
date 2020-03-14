#! /bin/python3

from psutil import cpu_times_percent
from psutil import virtual_memory
from psutil import swap_memory
from sys import argv

def ctp ():
    """Print CPU Usage."""
    cpu_d = cpu_times_percent(interval=1)._asdict()
    for key, value in cpu_d.items():
        print("system.cpu.",key,'\t', value)

def mem ():
    """Print Memory Usage."""
    vmem_d = virtual_memory()._asdict()
    for key, value in vmem_d.items():
        print("virtual \t", key,'\t', value)
    swmem_d = swap_memory()._asdict()
    for key, value in swmem_d.items():
        print("swap \t", key,'\t', value)

if "cpu" in argv:
    ctp()
elif "mem" in argv:
    mem()
else:
    print("Not supported argument. Please use [cpu|mem]\n")
