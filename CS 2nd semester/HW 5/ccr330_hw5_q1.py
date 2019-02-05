'''
Question	1:	Give	an	alternative	implementation	for	the	Queue	ADT.	
	Implementation	Requirements:	
     1. For	the	representation	of	Queue	objects,	your	data	members	should	be:	
         • Two	Stacks	–	of	type	ArrayStack	
         • Additional	O(1)	space	-	for	additional	data	members,	if	needed		
    2. Any	sequence	of	n	enqueue	and	dequeue	operations	(starting	with	an	empty	queue)	
    should	run	in	worst-case	of	O(n)	altogether.	
    
'''
class Empty(Exception):
    pass

class TwoArrayQueue:

    def __init__(self):
        self.stack_one = ArrayStack()
        self.stack_two = ArrayStack()
        
    def __len__(self):
        return len(self.stack_one)

    def is_empty(self):
        return len(self.stack_one) == 0

    def enqueue(self, elem):
        self.stack_one.push(elem)

    def dequeue(self):
        if (self.is_empty()):
            raise Empty("Queue is empty")
        for i in range((len(self.stack_one)) - 1): 
            self.stack_two.push(self.stack_one.pop())
        first_elem = self.stack_one.pop()
        for i in range(len(self.stack_two)): 
            self.stack_one.push(self.stack_two.pop())
        return first_elem
        
    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        for i in range((len(self.stack_one)) - 1): 
            self.stack_two.push(self.stack_one.pop())
        first_elem = self.stack_one.top()
        for i in range(len(self.stack_two)): 
            self.stack_one.push(self.stack_two.pop())
        return first_elem
        
                

class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.data.append(val)

    def top(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data[-1]

    def pop(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data.pop()
