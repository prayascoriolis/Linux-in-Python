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
import time
import grp
import pwd
from pathlib import Path
import stat

def format_mod_time(mod_time):
    """
    Convert the modification time (timestamp) of a file into a human-readable format.
    Args:
        mod_time (float): The modification time of the file as a Unix timestamp.
    Returns:
        str: The formatted modification time as a string, e.g., "Dec 17 14:32".
    """
    # Convert the timestamp
    mod_time_struct = time.localtime(mod_time)
    return time.strftime("%b %d %H:%M", mod_time_struct)

def get_user_group_names(st_uid, st_gid):
    """
    Retrieve the user and group names associated with the given user ID and group ID.
    Args:
        st_uid (int): The user ID of the file owner.
        st_gid (int): The group ID of the file owner.
    Returns:
        tuple: A tuple containing the user name (str) and the group name (str). 
               If an error occurs, returns a tuple with None and an error message.
    """
    try:
        # Get the group name using st_gid
        group_info = grp.getgrgid(st_gid)
        group_name = group_info.gr_name
        # Get the user name using st_uid
        user_info = pwd.getpwuid(st_uid)
        owner_name = user_info.pw_name
        return owner_name, group_name
    except Exception as e:
        return None, f"Error: {e}"

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
        return "directory."
    elif path_of_file.is_file():
        return "regular file."
    elif path_of_file.is_symlink():
        return "symbolic link."
    else:
        return "Unknown file type."

def ls_implement(path, long_list, file_type_info):
    """
    List the contents of a directory, with optional detailed information and file type information.
    Args:
        path (str): The path to the directory to list.
        long_list (bool): Flag to indicate whether detailed file information (-l) should be displayed.
        file_type_info (bool): Flag to indicate whether file type information (-F) should be displayed.
    Prints:
        The names of the files and directories, along with detailed information if applicable.
    """
    try:
        # list of all files in the dir
        entries = os.listdir(path)
        for entry in entries:
            full_path = os.path.join(path, entry) # complete path of each entry
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
                symbolic_permissions = stat.filemode(file_stat.st_mode) # permission in symbolic format
                size = file_stat.st_size # size in bytes
                mod_time = format_mod_time(file_stat.st_mtime) # time in M D H:M
                # Get the group name & user name
                owner_name, group_name = get_user_group_names(file_stat.st_uid, file_stat.st_gid)
                hard_link = file_stat.st_nlink # no. of hard links
                print(f"{symbolic_permissions} {hard_link} {group_name} {owner_name} {size} {mod_time} {file_type if file_type_info else ''}".strip())
    except Exception as e:
        print(f"Error: {e}")

def find(path, name):
    """
    Search for a file or directory by name within the specified path.
    Args:
        path (str): current dir
        name (str): The name of the file or directory to find.
    Prints:
        The full path of the found file/directory or a message if not found.
    """
    found = False
    for root, dirs, files in os.walk(path):
        if name in dirs or name in files:
            print(f"Found: {os.path.join(root, name)}")
            found = True
    if found is False:
        print(f"Not Found: {os.path.join(path,name)}")

def ln_implement(target, link, soft_link):
    """
    Create either a hard or soft (symbolic) link from a target file/directory to a new link.
    Args:
        target (str): The name of the target file or directory to link to.
        link (str): The name of the link to be created.
        soft_link (bool): If True, create a symbolic (soft) link; if False, create a hard link.
    Prints:
        A message indicating whether a hard or soft link was created.
    """
    try:
        # extracting dir name from target file
        target_dir_name = os.path.dirname(target)
        # making sure to add link file in same dir
        link_full_path = os.path.join(target_dir_name, link)
        # soft link
        if soft_link is True:
            os.symlink(target, link_full_path)
            print(f"Soft link created: {link_full_path} -> {target}")
        # hard link
        else:
            os.link(target, link_full_path)
            print(f"Hard link created: {link_full_path} -> {target}")
    except Exception as e:
        print(f"Error: {e}")

def rm_implement(name):
    """
    Remove a file or directory from the filesystem. If it's a symbolic link, it is removed directly.
    If it's a directory, the user is prompted before deletion if it's not empty.
    Args:
        name (str): The name of the file or directory to remove.
    Prints:
        A message indicating whether a file or directory was removed or if there was an error.
    """
    try:
        file_path = name
        # remove link
        if os.path.islink(file_path):
            os.remove(file_path)
            print(f"Symbolic link removed: {file_path}")
        # remove dir
        elif os.path.isdir(file_path):
            if len(os.listdir(file_path)) > 0:
                confirm = input(f"Directory {file_path} is not empty. Do you want to delete it? (y/n): ")
                if confirm.lower() == 'y':
                    os.rmdir(file_path)
                    print(f"Directory removed: {file_path}")
                else:
                    print("Operation canceled.")
            else:
                os.rmdir(file_path)
                print(f"Directory removed: {file_path}")
        # remove file
        else:
            os.remove(file_path)
            print(f"File removed: {file_path}")
    except Exception as e:
        print(f"Error: {e}")

def create_parser():
    """
    Create and return an argument parser for a file system explorer tool.
    Returns:
        argparse.ArgumentParser: The argument parser object with all subcommands and options.
    """
    parser = argparse.ArgumentParser(description="File system explorer.")
    # Define the main directory argument
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
    current_dir = os.getcwd()
    # Check which command was given and call the required function
    if args.command == "ls":
        l,f = args.l, args.F
        ls_implement(current_dir, l,f)
    elif args.command == "find":
        find(current_dir, args.name)
    elif args.command == "ln":
        s = args.s
        ln_implement(args.target, args.linkname, s)
    elif args.command == "rm":
        rm_implement(args.name)
    else:
        print("Invalid command.")

'''
USAGE:

 ls:
    1. python3 q1.py ls
    2. python3 q1.py ls -l
    3. python3 q1.py ls -F
    4. python3 q1.py ls -lF

 find:
    1. python3 q1.py find q2.py

 ln: 
    1. python3 q1.py ln -s ./test1/test2/x.txt soft_link.log
    2. python3 q1.py ln ./test1/test2/x.txt hard_link.log

 rm: 
    1. python3 q1.py rm ./test1/test2/x.txt
    2. python3 q1.py rm ./test1/test2
'''