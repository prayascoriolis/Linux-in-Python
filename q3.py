'''
Assignment 3: Process and Device Monitor

Description: Combine process and device monitoring into one program.

Requirements:

    Use psutil to list active processes with CPU, memory, and I/O statistics.
    Display connected devices (e.g., USB devices) and their mount points using /proc or lsblk.
    Implement a feature to monitor real-time changes to devices (e.g., using inotify or polling /dev for new device connections).
    Allow the user to terminate processes or safely eject devices.
'''

import psutil
import os
import subprocess
import time
import inotify.adapters
import sys

def display_active_process():
    '''
    Use psutil to list active processes with CPU, memory, and I/O statistics.
    '''
    print("Active Processes with CPU, Memory, and I/O Statistics:\n")
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info', 'io_counters']):
        try:
            print(f"PID: {proc.info['pid']}, Name: {proc.info['name']}, CPU: {proc.info['cpu_percent']}%, "
                  f"Memory: {proc.info['memory_info'].rss / (1024 * 1024):.2f} MB, "
                  f"I/O Read: {proc.info['io_counters'].read_bytes / (1024 * 1024):.2f} MB, "
                  f"I/O Write: {proc.info['io_counters'].write_bytes / (1024 * 1024):.2f} MB")
        except Exception as e:
            pass

def display_connected_devices():
    '''
    Display connected devices (e.g., USB devices) and their mount points using /proc or lsblk.
    '''
    print("\nConnected Devices and Mount Points:\n")
    # Using lsblk to get connected devices and their mount points
    try:
        result = subprocess.check_output("lsblk -o NAME,SIZE,MOUNTPOINT,TYPE", shell=True, text=True)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

def terminate_process(pid):
    '''
    Allow the user to terminate processes.
    '''
    try:
        proc = psutil.Process(pid)
        proc.terminate()
        print(f"Terminated process with PID: {pid}")
    except Exception as e:
        print(f"Error: {e}")

def eject_device(device):
    '''
    Allow the user to safely eject devices.
    '''
    """Eject the device."""
    try:
        subprocess.run(['sudo', 'eject', device], check=True)
        print(f"Device {device} ejected successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error ejecting device {device}: {e}")
        sys.exit(1)
    return

def real_time_monitoring():
    '''
    Implement a feature to monitor real-time changes to devices (e.g., using inotify or polling /dev for new device connections).
    '''
    import os
import time

def real_time_monitoring(dev_directory='/dev'):
    """Poll the /dev directory for device changes."""
    known_devices = set(os.listdir(dev_directory))
    while True:
        time.sleep(1)  # Poll every 1 second
        current_devices = set(os.listdir(dev_directory))
        added_devices = current_devices - known_devices
        removed_devices = known_devices - current_devices
        for device in added_devices:
            print(f"New device connected: {dev_directory}/{device}")
        for device in removed_devices:
            print(f"Device disconnected: {dev_directory}/{device}")
        known_devices = current_devices

def menu():
    print("Please choose an option:")
    print("1. Display active processes")
    print("2. Display connected devices")
    print("3. Terminate a process")
    print("4. Eject a device")
    print("5. Real-time monitoring of devices")
    print("6. Exit")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter the number of your choice: ").strip()
        if choice == "1":
            display_active_process()
        elif choice == "2":
            display_connected_devices()
        elif choice == "3":
            pid = int(input("\nEnter PID of the process to terminate: "))
            terminate_process(pid)
        elif choice == "4":
            device = input("\nEnter the device name to eject (e.g., sdb1): ")
            eject_device(device)
        elif choice == "5":
            real_time_monitoring()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
