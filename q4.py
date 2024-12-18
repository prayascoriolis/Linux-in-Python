'''
Assignment 4: File Metadata and Permission Manager

Description: Build a program to manage file metadata and permissions interactively.

Requirements:
    Display and edit metadata (e.g., creation, modification times).
    Display current file permissions in symbolic (-rw-r--r--) and octal (644) formats.
    Allow permission changes using symbolic (chmod u+x) and numeric (chmod 755) notations.
    Display the owner and group of a file, and provide an option to change them (chown).
'''

import argparse
import os
import time
import grp
import pwd
from pathlib import Path
import stat
from datetime import datetime

def get_permission(path):
    """
    List the permission of a file.
    Args:
        path (str): The path to the file
    Prints:
        The names of the files & permission
    """
    try:
        # list of all files in the dir
        file_stat = os.stat(path)
        print("\n")
        print(path, end=" ")
        permission_num = oct(file_stat.st_mode)[-3:] # permission in numerical format
        permission_symbolic = stat.filemode(file_stat.st_mode)
        print(f"{permission_symbolic} {permission_num}")
    except Exception as e:
        print(f"Error: {e}")

def display_metadata(file_path):
    """
    List the meta data of a file.
    Args:
        path (str): The path to the file
    Prints:
        The names of the files & metadata:
        file, size, modify time, access time
        & created time
    """
    try:
        file_stats = os.stat(file_path)
        # Display file metadata
        print("\n")
        print(f"File: {file_path}")
        print(f"Size: {file_stats.st_size} bytes")
        print(f"Last modified: {time.ctime(file_stats.st_mtime)}")
        print(f"Last accessed: {time.ctime(file_stats.st_atime)}")
        print(f"Created: {time.ctime(file_stats.st_ctime)}")
    except Exception as e:
        print(f"Error: {e}")

def change_permissions(file_path, permission_str):
    try:
        # Check if permission_str is numeric or symbolic
        if permission_str.isnumeric():
            permissions = int(permission_str, 8)
            os.chmod(file_path, permissions)
            print(f"Permissions for {file_path} changed to {permission_str} (Octal).")
        else:
            os.system(f"chmod {permission_str} {file_path}")
            print(f"Permissions for {file_path} changed to {permission_str} (Symbolic).")
    except Exception as e:
        print(f"Error: {e}")

def display_owner_group(file_path):
    """
    List the owner & group of a file.
    Args:
        path (str): The path to the file
    Prints:
        The names group & owner of file
    """
    try:
        # Display file owner and group
        file_stat = os.stat(file_path)
        # Get the group name using st_gid
        group_info = grp.getgrgid(file_stat.st_gid)
        group_name = group_info.gr_name
        # Get the user name using st_uid
        user_info = pwd.getpwuid(file_stat.st_uid)
        owner_name = user_info.pw_name
        print(f"\nFile name: {file_path}")
        print(f"Owner: {owner_name}")
        print(f"Group: {group_name}")
    except Exception as e:
        print(f"Error: {e}")

def change_owner_group(file_path, owner_name, group_name):
    """
    Change the owner & group of a file.
    Args:
        path (str): The path to the file
    Prints:
        The names group & owner of file
    """
    try:
        owner_uid = pwd.getpwnam(owner_name).pw_uid
        group_gid = grp.getgrnam(group_name).gr_gid
        os.chown(file_path, owner_uid, group_gid)
        print(f"Owner and Group for {file_path} changed to {owner_name} and {group_name}.")
    except Exception as e:
        print(f"Error: {e}")

def change_metadata(file_path, access_time=None, modify_time=None):
    """
    Change the meta data of a file.
    Args:
        path (str): The path to the file
        access_time(str): new access time
        modify_time(str): new modify time
    Process:
        Changes access or modify time
    """
    try:
        # Convert provided time strings to timestamp
        file_stats = os.stat(file_path)
        if access_time is not None:
            access_time = datetime.strptime(access_time, '%Y-%m-%d %H:%M:%S').timestamp()
        else:
            # if access time is provided blank by user, current access time is used
            access_time = file_stats.st_atime
        if modify_time is not None:
            modify_time = datetime.strptime(modify_time, '%Y-%m-%d %H:%M:%S').timestamp()
        else:
            # if modify time is provided blank by user, current modify time is used
            modify_time = file_stats.st_mtime
        # Update the file's access and modification times
        os.utime(file_path, (access_time, modify_time))
        print(f"Metadata for {file_path} updated")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    while True:
        print("\nFile Management Menu:")
        print("1. Display and edit metadata")
        print("2. Edit file metadata (last access and modification times)")
        print("3. Display current file permissions in symbolic and numerical formats.")
        print("4. Allow permission changes using symbolic (chmod u+x) and numeric (chmod 755) notations.")
        print("5. Display the owner and group of a file.")
        print("6. Change owner and group of file.")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            file_path = input("Enter file path: ")
            display_metadata(file_path)
        elif choice == "2":
            file_path = input("Enter file path: ")
            access_time = input("Enter new access time (YYYY-MM-DD HH:MM:SS, leave blank to keep current): ")
            modify_time = input("Enter new modify time (YYYY-MM-DD HH:MM:SS, leave blank to keep current): ")
            # If input is blank pass None to keep the current values
            change_metadata(file_path, access_time or None, modify_time or None)
        elif choice == "3":
            file_path = input("Enter the file path: ").strip()
            get_permission(file_path)
        elif choice == "4":
            file_path = input("Enter file path: ")
            permission_str = input("Enter new permissions (numeric or symbolic): ")
            change_permissions(file_path, permission_str)
        elif choice == "5":
            file_path = input("Enter file path: ")
            display_owner_group(file_path)
        elif choice == "6":
            file_path = input("Enter file path: ")
            owner_name = input("Enter new owner name: ")
            group_name = input("Enter new group name: ")
            change_owner_group(file_path, owner_name, group_name)
        elif choice == "7":
            print("Exiting File Management.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

'''
==== USAGE ====


1. Display and edit metadata
Select: 1
Enter file path: /path/to/your/file.txt


2. Edit file metadata (last access and modification times)
Select: 2
Enter file path: /path/to/your/file.txt
Enter new access time (YYYY-MM-DD HH:MM:SS, leave blank to keep current): 2024-12-18 15:00:00
Enter new modify time (YYYY-MM-DD HH:MM:SS, leave blank to keep current): 2024-12-18 15:05:00


3. Display current file permissions in symbolic and numerical formats.
Select: 3
Enter file path: /path/to/your/file.txt


4. Change permission using symbolic (chmod u+x) and numeric (chmod 755) notations.
Select: 4
Enter file path: /path/to/your/file.txt
Enter new permissions (numeric or symbolic): 755 OR u+x


5. Display the owner and group of a file.
Select: 5
Enter file path: /path/to/your/file.txt


6. Change owner and group of file.
Select: 6
run python script as sudo to change owner & group name
Enter file path: /path/to/your/file.txt
Enter new owner name: newuser name
Enter new group name: newgroup name


7. Exit
Select: 7 to quit

'''