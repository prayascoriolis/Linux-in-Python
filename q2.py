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

import psutil
import subprocess

def display_disk_info():
    '''
    Disk Partition Menu
    '''
    # Return all mounted disk partitions as a list of named tuples including device,
    # mount point and filesystem type.
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"=== Partition: {partition.device} ===")
        try:
            total, used, free, percent = psutil.disk_usage(partition.mountpoint)
            print(f"Mountpoint: {partition.mountpoint}")
            print(f"Total: {total / (1024**3):.2f} GB")
            print(f"Used:  {used / (1024**3):.2f} GB")
            print(f"Free:  {free / (1024**3):.2f} GB")
            print(f"Percent Used:  {percent:.2f} %")
            print(f"File type:  {partition.fstype}\n")
        except PermissionError:
            print("Access Denied\n")

def mount_device(device, mountpoint):
    '''
    mounting operation
    device: ex- /dev/sda3
    mountpoint: ex- /mnt/
    *** make sure the device is partitoned and filesystem assigned ***
    '''
    try:
        subprocess.run(['sudo', 'mount', device, mountpoint], check=True)
        print(f"Device {device} successfully mounted at {mountpoint}.")
    except subprocess.CalledProcessError as e:
        print(f"Error mounting: {e}")

def unmount_device(device):
    '''
    unmounting
    device: ex- /dev/sda3
    '''
    try:
        subprocess.run(['sudo', 'umount', device], check=True)
        print(f"Device {device} successfully unmounted.")
    except subprocess.CalledProcessError as e:
        print(f"Error unmounting: {e}")

def format_device(device, filesystem):
    '''
    changing format of a filesystem
    device: ex- /dev/sda3
    filesystem (new): ex- 'ext4', 'vfat', 'ntfs', 'ext3'
    '''
    try:
        valid_filesystems = ['ext4', 'vfat', 'ntfs', 'ext3']
        if filesystem not in valid_filesystems:
            print(f"Unsupported filesystem: {filesystem}. Choose from {valid_filesystems}.")
            return
        print(f"Warning: Formatting {device} will erase all data!")
        confirm = input("Type 'YES' to proceed: ").strip()
        if confirm != 'YES':
            print("Operation cancelled.")
            return
        subprocess.run(['sudo', f'mkfs.{filesystem}', device], check=True)
        print(f"{device} successfully formatted to {filesystem}.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    while True:
        print("\nDisk Management Menu:")
        print("1. Display Disk Info")
        print("2. Mount a Device")
        print("3. Unmount a Device")
        print("4. Format a Device")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            display_disk_info()
        elif choice == "2":
            device = input("Enter the device path (in /dev/): ").strip()
            mountpoint = input("Enter the mountpoint (in /mnt/): ").strip()
            mount_device(device, mountpoint)
        elif choice == "3":
            device = input("Enter the device path to unmount (e.g., /dev/sdb1): ").strip()
            unmount_device(device)
        elif choice == "4":
            device = input("Enter the device path to format (in /dev/): ").strip()
            filesystem = input("Enter filesystem type (ext4, vfat etc): ").strip()
            format_device(device, filesystem)
        elif choice == "5":
            print("Exiting Disk Management.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
