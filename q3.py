'''
Assignment 3: Process and Device Monitor

Description: Combine process and device monitoring into one program.

Requirements:

    Use psutil to list active processes with CPU, memory, and I/O statistics.
    Display connected devices (e.g., USB devices) and their mount points using /proc or lsblk.
    Implement a feature to monitor real-time changes to devices (e.g., using inotify or polling /dev for new device connections).
    Allow the user to terminate processes or safely eject devices.
'''