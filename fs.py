'''Assignment 1: Advanced File System Explorer

Description: Extend the basic file system explorer to include
advanced features like handling symbolic links and detecting file types.

Requirements:

    Use os, os.path, and stat modules.
    Implement commands:
        ls with options to display file types (-F) and detailed information (-l).
        find <name> to search for files/directories recursively from the current directory.
        ln -s <target> <linkname> to create symbolic links.
    Handle and display symbolic links properly.
    Provide an option to delete files and directories safely (rm <name>).
'''
import argparse
import os
import stat
import sys
import time
import grp
import pwd
from pathlib import Path

def format_mod_time(mod_time):
    # Convert the timestamp
    mod_time_struct = time.localtime(mod_time)
    return time.strftime("%b %d %H:%M", mod_time_struct)

def get_user_group_names(st_uid, st_gid):
    try:
        # Get the group name using st_gid
        group_info = grp.getgrgid(st_gid)
        group_name = group_info.gr_name
        # Get the user name using st_uid
        user_info = pwd.getpwuid(st_uid)
        user_name = user_info.pw_name
        return user_name, group_name
    except Exception as e:
        return None, f"Error: {e}"

def check_file_type(path):
    p = Path(path)
    if p.is_dir():
        return "directory."
    elif p.is_file():
        return "regular file."
    elif p.is_symlink():
        return "symbolic link."
    else:
        return "Unknown file type."

def ls(path, long_list, file_type_info):
    try:
        # list of all files in the dir
        entries = os.listdir(path)
        for entry in entries:
            full_path = os.path.join(path, entry)
            file_stat = os.stat(full_path)
            # if both -l and -F is false, only files are listed
            print(entry, end=" ")
            # Handle file type detection (-F)
            if file_type_info is True:
                file_type = check_file_type(full_path)
                if long_list is not True:
                    print(file_type)
            # Handle detailed information (-l)
            if long_list is True:
                permissions = oct(file_stat.st_mode)[-3:] # permission in numerical format
                size = file_stat.st_size # size in bytes
                mod_time = format_mod_time(file_stat.st_mtime) # time in M D H:M
                # Get the group name & user name
                group_name, user_name = get_user_group_names(file_stat.st_uid, file_stat.st_gid)
                hard_link = file_stat.st_nlink # no. of hard links
                print(f"{permissions} {hard_link} {group_name} {user_name} {size} {mod_time} {file_type if file_type_info else ''}".strip())
    except Exception as e:
        print(f"Error: {e}")

def find(path, name):
    found = False
    for root, dirs, files in os.walk(path):
        if name in dirs or name in files:
            print(f"Found: {os.path.join(root, name)}")
            found = True
    if found is False:
        print(f"Not Found: {os.path.join(path,name)}")

def ln(target, link, soft_link, path):
    try:
        target_full_path = os.path.join(path, target)
        link_full_path = os.path.join(path, link)
        if soft_link is True:
            os.symlink(target_full_path, link_full_path)
            print(f"Soft link created: {link_full_path} -> {target_full_path}")
        else:
            os.link(target_full_path, link_full_path)
            print(f"Hard link created: {link_full_path} -> {target_full_path}")
    except Exception as e:
        print(f"Error: {e}")

def rm(name, path):
    try:
        full_path = os.path.join(path, name)
        if os.path.islink(full_path):
            os.remove(full_path)
            print(f"Symbolic link removed: {full_path}")
        elif os.path.isdir(full_path):
            if len(os.listdir(full_path)) > 0:
                confirm = input(f"Directory {full_path} is not empty. Do you want to delete it? (y/n): ")
                if confirm.lower() == 'y':
                    os.rmdir(full_path)
                    print(f"Directory removed: {full_path}")
                else:
                    print("Operation canceled.")
            else:
                os.rmdir(full_path)
                print(f"Directory removed: {full_path}")
        else:
            os.remove(full_path)
            print(f"File removed: {full_path}")
    except Exception as e:
        print(f"Error: {e}")

def create_parser():
    parser = argparse.ArgumentParser(description="File system explorer.")
   
    # Define the main directory argument
    parser.add_argument(
        "dir",
        nargs="?",
        default="./",
        help="Directory path"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Subparser for `ls`
    ls_parser = subparsers.add_parser("ls", help="List directory contents")
    ls_parser.add_argument(
        "-l",
        action="store_true",
        help="Display detailed information about files"
    )
    ls_parser.add_argument(
        "-F",
        action="store_true",
        help="Display file types (e.g., / for directories, * for executables)"
    )

    # Subparser for `find`
    find_parser = subparsers.add_parser("find", help="Find a file or directory")
    find_parser.add_argument("name", help="Name of the file/directory to find")

    # Subparser for `ln`
    ln_parser = subparsers.add_parser("ln", help="Create a symbolic link")
    ln_parser.add_argument( "-s", action="store_true", help="flag to determine hard or soft link")
    ln_parser.add_argument("target", help="Target file or directory")
    ln_parser.add_argument("linkname", help="Link name")

    # Subparser for `rm`
    rm_parser = subparsers.add_parser("rm", help="Remove a file or directory")
    rm_parser.add_argument("name", help="File or directory to remove")

    return parser

if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    # Check which command was given and call the required function
    if args.command == "ls":
        print(args.dir, args.l, args.F)
        l,f = args.l, args.F
        ls(args.dir, l,f)
    elif args.command == "find":
        find(args.dir, args.name)
    elif args.command == "ln":
        s = args.s
        dir = args.dir
        ln(args.target, args.linkname, s, dir)
    elif args.command == "rm":
        rm(args.name, args.dir)
    else:
        print("Invalid command.")

