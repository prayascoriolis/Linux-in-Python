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

def get_symbolic_permission(permission_num):
    permission_map = {
        '0': '---',  # No permissions
        '1': '--x',  # Execute
        '2': '-w-',  # Write
        '3': '-wx',  # Write and execute
        '4': 'r--',  # Read
        '5': 'r-x',  # Read and execute
        '6': 'rw-',  # Read and write
        '7': 'rwx'   # Read, write, and execute
    }
    # Split the permission_num into three parts: user, group, others
    user, group, others = permission_num
    # Get the symbolic representation for each part
    symbolic_permission = permission_map[user] + permission_map[group] + permission_map[others]
    symbolic_permission = "-"+symbolic_permission
    return symbolic_permission

def check_file_type(path):
    """
    Check and return the type of the file at the given path (directory, regular file, symbolic link, or unknown).
    Args:
        path (str): The path to the file or directory.
    Returns:
        str: A string describing the file type ("directory", "regular file", "symbolic link", or "Unknown file type").
    """
    path_of_file = Path(path)
    if path_of_file.is_dir():
        return "d"
    elif path_of_file.is_file():
        return "-"
    elif path_of_file.is_symlink():
        return "l"
    else:
        return "-"

def get_permission(path):
    """
    List the contents of a directory, with optional detailed information and file type information.
    Args:
        path (str): The path to the directory to list.
    Prints:
        The names of the files and directories, along with detailed information if applicable.
    """
    try:
        # list of all files in the dir
        entries = os.listdir(path)
        for entry in entries:
            full_path = os.path.join(path, entry) # complete path of each entry
            file_stat = os.stat(full_path)
            print(entry, end=" ")
            file_type = check_file_type(full_path)
            permission_num = oct(file_stat.st_mode)[-3:] # permission in numerical format
            permission_symbolic = get_symbolic_permission(permission_num) # permission in symbolic format
            permission_symbolic = permission_symbolic.replace('-', file_type, 1) # appending file type
            print(f"{permission_symbolic}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    while True:
        print("\nFile Management Menu:")
        print("1. Display and edit metadata (e.g., creation, modification times).")
        print("2. Display current file permissions in symbolic (-rw-r--r--) and octal (644) formats.")
        print("3. Allow permission changes using symbolic (chmod u+x) and numeric (chmod 755) notations.")
        print("4. Display the owner and group of a file, and provide an option to change them (chown).")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            print('hehe')
        elif choice == "2":
            dir_path = input("Enter the dir path: ").strip()
            get_permission(dir_path)
        elif choice == "3":
            device = input("Enter the device path to unmount (e.g., /dev/sdb1): ").strip()
        elif choice == "4":
            device = input("Enter the device path to format (in /dev/): ").strip()
        elif choice == "5":
            print("Exiting File Management.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
