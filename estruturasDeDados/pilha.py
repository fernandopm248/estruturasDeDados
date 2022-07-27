
from ctypes import pointer

class Node :
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack :
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self,elem):
        node = Node(elem)
        node.next = self.top #next é o elemento abaixo do atual
        self.top = node
        self.size += 1

    def pop(self):
        if self.size > 0 :
            node = self.top
            self.top =  self.top.next
            self.size -= 1
            return node
        raise IndexError('stack is empty')    

    def peek(self):
        if self.size > 0 :
            return self.top.data
          
        raise IndexError('stack is empty')       
    


    def __len__(self) :
        return self.size

    def __repr__(self):
       r = ''
       pointer = self.top
       while(pointer):
           r = r + str(pointer.data) + "\n"
           pointer = pointer.next
       return r   
    def __str__(self):
        return self.__repr__()

if __name__ == "__main__":
    pilha = Stack()
    print(len(pilha))
    pilha.push(5)
    pilha.push('sssss')
    pilha.push(True)
    pilha.push(5.5)
    pilha.push(99)
    # print(pilha,'\n')
    # print(pilha.peek(),'aaaaaaa')
    pilha.pop()
    print(pilha,'\n')
    pilha.pop()
    print(pilha,'\n')
    pilha.pop()
    print(pilha,'\n')
    pilha.pop()
    print(pilha,'\n')
    pilha.pop()
    print(pilha,'\n')
    pilha.pop()
    print(pilha,'\n')