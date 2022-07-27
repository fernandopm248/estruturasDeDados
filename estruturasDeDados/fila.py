
from ctypes import pointer
import queue

class Node :
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue :
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def push(self,elem):
        node = Node(elem)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node    

        if self.first is None :
            self.first = node

        self.size += 1


    def pop(self):
        if self.size > 0 :
            elem = self.first.data
            self.first = self.first.next 
            self.size -= 1
            return elem
        raise IndexError('queue is empty')    

    def peek(self):
        if self.size > 0 :
            elem = self.first.data         
            return elem
        raise IndexError('queue is empty')
    


    def __len__(self) :
        return self.size

    def __repr__(self):
        if self.size > 0 :
            r = ''
            pointer = self.first
            while(pointer):
                r = r + str(pointer.data) + " "
                pointer = pointer.next
            return r   
        return 'empty queue'    
    def __str__(self):
        return self.__repr__()

fila = Queue()
fila.push(1)
fila.push(1.5)
fila.push(True)
fila.push('atuesta')
print(fila , '\n')
fila.pop()
print(fila , '\n')
fila.pop()
print(fila , '\n')
fila.peek()
print(fila.peek() , '\n')
fila.push(5)
print(fila , '\n')
print(fila.pop())
print(len(fila))