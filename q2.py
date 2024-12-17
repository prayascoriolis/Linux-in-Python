'''
Assignment 2: Disk and Partition Manager
Description: Develop a Python program to display and manage disk partitions.
Requirements:

    Use the os and shutil modules to display available disks and partitions.
    Integrate psutil to fetch details such as:
        Total space, used space, and free space.
        Mount points.
        File system type.
    Allow users to mount or unmount devices using system commands (subprocess).
    Provide a feature to format a device to a specified file system (e.g., ext4, xfs).
'''
import argparse
import os
import time
import grp
import pwd
from pathlib import Path

