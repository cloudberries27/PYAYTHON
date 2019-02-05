# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:22:52 2017

@author: Claudia Rodriguez
"""
class Empty(Exception):
    pass

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
        
class ArrayDeque:
    INITIAL_CAPACITY = 10
    
    def __init__(self):
        self.data = [None] * ArrayDeque.INITIAL_CAPACITY
        self.size = 0
        self.front = 0
        
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
        
    def first(self):
        if self.is_empty():
            raise Empty('Queue empty!')
        return self.data[self.front]
        
    def last(self):
        if self.is_empty():
            raise Empty('Queue empty!')
        back = (self.front + self.size - 1) % len(self.data)
        return self.data[back]
        
    def delete_first(self):
        if self.is_empty():
            raise Empty('Queue empty!')
        value = self.data[self.front]
        self.front=(self.front+1) % len(self.data)
        self.size -= 1
        return value
        
    def delete_last(self):
        if self.is_empty():
            raise Empty('Queue empty!')
        size = self.size
        back_ind = (self.front + size - 1) % len(self.data)
        value = self.data[back_ind]
        self.size -= 1
        return value
        
    def add_last(self, element):
        if self.size == len(self.data):
            self.resize(2*len(self.data))
        avail = (self.front + self.size) % len(self.data)
        self.data[avail] = element
        self.size += 1
        
    def add_first(self,element):
        if self.size == len(self.data):
            self.resize(2*len(self.data))
        self.front = (self.front - 1) % len(self.data)
        self.data[self.front] = element
        self.size += 1
        
    def resize(self,cap):
        old = self.data
        self.data = [None] *cap
        walk = self.front
        for k in range(self.size):
            self.data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self.front = 0
    
variable_dict = {}
def postfix_calculator():
    value = ''
    
    while value != "done()":
        
        value = input("--> ")
        main_deque = ArrayDeque()
        stack_operations = ArrayStack()
        
        value = value.split(" ")
        value = ''.join(value)
        
        if value == "done()":
            return
            
        if len(value) > 1 and value[0].isalpha() and value[1] == "=":   #How "x =" and "y = " works
            Notation = value[0]
            value = value[2:]
            result = calculation(value,main_deque,stack_operations)
            variable_dict[Notation] = result
            print(Notation)
            
        elif len(value) == 1 and value[0].isalpha():
            Notation = value[0]
            print(variable_dict[Notation])
            
        else:
            result = calculation(value,main_deque,stack_operations)
            print(result)
    
    
#Helper function to do calculations    
def calculation(value, main_deque, stack_operations):
    for element in value:
        main_deque.add_last(element)
            
    for i in range(len(main_deque)):
        consider = main_deque.delete_first()
        if consider.isdigit():
            stack_operations.push(int(consider))
            
        elif consider.isalpha():
            if consider in variable_dict:
                Calling = variable_dict[consider]
                stack_operations.push(int(Calling))
            else:
                return False
            
        else:
            if consider == "+":
                number1 = stack_operations.pop()
                number2 = stack_operations.pop()
                number3 = number1 + number2
                stack_operations.push(number3)
                
            elif consider == "*":
                number1 = stack_operations.pop()
                number2 = stack_operations.pop()
                number3 = number1 * number2
                stack_operations.push(number3)
                
            elif consider == "/":
                number1 = stack_operations.pop()
                number2 = stack_operations.pop()
                number3 = number2 / number1
                stack_operations.push(number3)
                
            elif consider == "-":
                number1 = stack_operations.pop()
                number2 = stack_operations.pop()
                number3 = number2 - number1
                stack_operations.push(number3)
    result = stack_operations.pop()
    return result
