'''24. Create a program to implement a priority queue using a binary heap.'''

class PriorityQueue:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def insert(self, value):
        # Insert a value into the priority queue.
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        # Remove and return the smallest element (root) from the heap.
        if not self.heap:
            raise IndexError("The priority queue is empty!")
        
        root = self.heap[0]
        # Replace the root with the last element
        self.heap[0] = self.heap.pop()
        # Restore the heap property
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        # Restore the heap property by shifting the element at 'index' upwards.
        while index > 0 and self.heap[index] < self.heap[self.parent(index)]:
            # Swap with parent
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)

    def _heapify_down(self, index):
        # Restore the heap property by shifting the element at 'index' downwards.
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)
        
        # Check if left child is smaller
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        # Check if right child is smaller
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        # Swap and continue heapifying if needed
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def peek(self):
        # Get the smallest element without removing it.
        if not self.heap:
            raise IndexError("The priority queue is empty!")
        return self.heap[0]

    def is_empty(self):
        return len(self.heap) == 0

if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert(10)
    pq.insert(5)
    pq.insert(20)
    pq.insert(2)
    print("Peek:", pq.peek())
    print("Extract Min:", pq.extract_min())
    print("Extract Min:", pq.extract_min())
    print("Is Empty:", pq.is_empty())
