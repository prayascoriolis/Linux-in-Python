'''
Assignment 5: Virtual File System Simulator

Description: Create a Python program to simulate a basic virtual file system (VFS).

Requirements:

    Represent the VFS as a tree structure in memory.
    Implement commands:
        mkdir <name> to create directories.
        touch <name> to create files.
        rm <name> to delete files or directories.
        mv <source> <destination> to move/rename files or directories.
        ls and pwd commands as in a real file system.
    Add basic read and write operations to virtual files.
'''

class VirtualFile:
    def __init__(self, name):
        self.name = name
        self.content = ""
        self.type = "file"

    def write(self, content):
        """Simulate writing content to the virtual file."""
        self.content = content

    def read(self):
        """Simulate reading the content of the virtual file."""
        return self.content


class VirtualDirectory:
    def __init__(self, name, parent=None):
        self.name = name
        self.type = "directory"
        self.children = {}
        self.parent = parent  # Parent directory reference

    def add(self, name, entity):
        """Add a file or directory to this directory."""
        self.children[name] = entity

    def remove(self, name):
        """Remove a file or directory from this directory."""
        if name in self.children:
            del self.children[name]

    def get(self, name):
        """Get a file or directory by name."""
        return self.children.get(name)

    def list(self):
        """List all files and directories in this directory."""
        return self.children.keys()

    def full_path(self):
        """Return the full path of this directory."""
        if self.parent:
            return self.parent.full_path() + "/" + self.name
        return "/"  # root directory

    def display_tree(self, prefix=""):
        """Recursively display the directory tree structure."""
        print(f"{prefix}📂 {self.name}")
        for child_name, child in self.children.items():
            if child.type == "directory":
                child.display_tree(prefix + "    ")
            else:
                print(f"{prefix}    📄 {child_name}")


class VirtualFileSystem:
    def __init__(self):
        self.root = VirtualDirectory('/')
        self.current_directory = self.root

    def mkdir(self, path):
        """Create a new directory at a specified path."""
        path_parts = path.strip('/').split('/')
        current = self.root
        for part in path_parts:
            print(part, current.name, current.children)
            if part not in current.children:
                current.add(part, VirtualDirectory(part, current))
            current = current.children[part]
        print(f"Directory '{path}' created.")

    def touch(self, name):
        """Create a new file."""
        if name in self.current_directory.children:
            print(f"File '{name}' already exists.")
        else:
            self.current_directory.add(name, VirtualFile(name))
            print(f"File '{name}' created.")

    def rm(self, name):
        """Remove a file or directory."""
        if name in self.current_directory.children:
            self.current_directory.remove(name)
            print(f"'{name}' removed.")
        else:
            print(f"'{name}' not found.")

    def mv(self, source, destination):
        """Move or rename a file or directory."""
        source_entity = self.current_directory.get(source)
        if source_entity:
            self.current_directory.remove(source)
            self.current_directory.add(destination, source_entity)
            print(f"'{source}' moved/renamed to '{destination}'.")
        else:
            print(f"'{source}' not found.")

    def ls(self, path=None):
        """List contents of the current directory or a specific path."""
        if path is None or path == ".":
            target_directory = self.current_directory
        else:
            target_directory = self.get_directory(path)

        if target_directory:
            contents = target_directory.list()
            if contents:
                print(" ".join(contents))
            else:
                print("Directory is empty.")
        else:
            print(f"'{path}' is not a valid directory.")

    def pwd(self):
        """Print the current working directory."""
        print(self.current_directory.full_path())

    def read_file(self, name):
        """Read the content of a virtual file."""
        file = self.current_directory.get(name)
        if isinstance(file, VirtualFile):
            print(file.read())
        else:
            print(f"'{name}' is not a file.")

    def write_file(self, name, content):
        """Write content to a virtual file."""
        file = self.current_directory.get(name)
        if isinstance(file, VirtualFile):
            file.write(content)
            print(f"Content written to '{name}'.")
        else:
            print(f"'{name}' is not a file.")

    def tree(self):
        """Display the directory structure as a tree."""
        print("Virtual File System Tree:")
        self.root.display_tree()

    def get_directory(self, path):
        """Navigate to a directory given its absolute path."""
        path_parts = path.strip('/').split('/')
        current = self.root
        for part in path_parts:
            if part in current.children and current.children[part].type == "directory":
                current = current.children[part]
            else:
                return None
        return current


def main():
    vfs = VirtualFileSystem()
    print("Welcome to the Real-Time Virtual File System! Type 'exit' to quit.")

    while True:
        command = input("VFS> ").strip()
        if command.lower() == "exit":
            print("Exiting the Virtual File System. Goodbye!")
            break

        parts = command.split()
        if not parts:
            continue

        cmd = parts[0]
        args = parts[1:]

        if cmd == 'mkdir' and len(args) == 1:
            vfs.mkdir(args[0])

        elif cmd == 'touch' and len(args) == 1:
            vfs.touch(args[0])

        elif cmd == 'rm' and len(args) == 1:
            vfs.rm(args[0])

        elif cmd == 'mv' and len(args) == 2:
            vfs.mv(args[0], args[1])

        elif cmd == 'ls':
            path = args[0] if args else None
            vfs.ls(path)

        elif cmd == 'pwd':
            vfs.pwd()

        elif cmd == 'read' and len(args) == 1:
            vfs.read_file(args[0])

        elif cmd == 'write' and len(args) == 2:
            vfs.write_file(args[0], args[1])

        elif cmd == 'tree':
            vfs.tree()

        else:
            print("Invalid command. Try again.")


if __name__ == "__main__":
    main()



''' 
USAGE:

python q5.py mkdir mydir        # Create directory 'mydir'

python q5.py mkdir subdir       # Create 'subdir' inside the current directory

python q5.py touch myfile.txt   # Create file 'myfile.txt'

python q5.py ls                 # List contents of current directory

python q5.py pwd                # Show the full path of the current directory

python q5.py mv myfile.txt myfile2.txt  # Rename 'myfile.txt' to 'myfile2.txt'

python q5.py rm myfile2.txt     # Remove 'myfile2.txt'

python q5.py ls /mydir          # List contents of 'mydir' (absolute path)

'''
