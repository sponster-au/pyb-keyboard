#! /usr/bin/env python3
import sys
from shutil import copyfile
import subprocess
import time

pyb = "/Volumes/PYBFLASH"

for i, arg in enumerate(sys.argv[1:]):
    if i == 0:
        copyfile(arg, pyb + "/main.py")
    else:
        copyfile(arg, pyb + "/" + arg)
time.sleep(10)
subprocess.call("diskutil unmountDisk /dev/disk2".split())
time.sleep(10)
print("press pyboard reset button now")
