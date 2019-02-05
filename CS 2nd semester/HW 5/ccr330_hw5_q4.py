"""
Give a Python implementation for the MaxStack ADT
"""
class Empty(Exception):
    pass


class MaxStack:
    def __init__(self):
        self.data = []
        self.duplicate = [0]
        
    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.data.append(val)
        if self.top() >= self.duplicate[-1]:
            self.duplicate.append(val)

    def top(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data[-1]

    def pop(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data.pop()
    
    def max(self):
        return self.duplicate.pop()
        
        
def main():
    maxS = MaxStack()
    maxS.push(3)
    maxS.push(1)
    maxS.push(6)
    maxS.push(4)
    print(maxS.max())
    print(maxS.pop())
    print(maxS.pop())
    print(maxS.max())
main()