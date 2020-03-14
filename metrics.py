#! /bin/python3

from psutil import cpu_times_percent
from psutil import virtual_memory
from psutil import swap_memory
from sys import argv

def ctp ():
    """Print CPU Usage."""
    CPU_D = cpu_times_percent(interval=1)._asdict()
    for key, value in CPU_D.items():
        print("system.cpu.",key,'\t', value)

def mem ():
    """Print Memory Usage."""
    VMEM_D = virtual_memory()._asdict()
    for key, value in VMEM_D.items():
        print("virtual \t", key,'\t', value)
    SwMEM_D = swap_memory()._asdict()
    for key, value in SwMEM_D.items():
        print("swap \t", key,'\t', value)


if "cpu" in argv:
    ctp()
elif "mem" in argv:
    mem()
else:
    print("Not supported argument. Please use [cpu|mem]\n")
