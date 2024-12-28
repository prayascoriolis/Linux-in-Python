'''15. Write a function to solve the Tower of Hanoi problem for n disks.'''

def tower_of_hanoi(n, source, auxiliary, target):
    if n > 0:
        # Move n-1 disks from A to B using 
        tower_of_hanoi(n - 1, source, target, auxiliary)
        # Move the nth disk from A to 
        print(f"Move disk {n} from {source} to {target}")
        # Move the n-1 disks from B to C using 
        tower_of_hanoi(n - 1, auxiliary, source, target)

n = 3
# A, B, C are source, auxiliary, target respectively
tower_of_hanoi(n, 'A', 'B', 'C')
