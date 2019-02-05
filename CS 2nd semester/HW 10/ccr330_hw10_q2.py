import heap.py
class Empty(Exception):
    pass

class ArrayQueue:

    def __init__(self):
        self.data = heap.py.ArrayMinHeap()
        self.maxKey = 0

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return (len(self.data) == 0)

    def enqueue(self, elem):
        self.data.insert(self.maxKey, elem)
        self.maxKey += 1

    def dequeue(self):
        self.data.delete_min()
        self.maxKey -= 1

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.data.min()

