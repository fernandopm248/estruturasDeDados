


class Node :
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist :
    def __init__(self,) :
        self.head = None
        self.size = 0

    def append(self,elem)   :
        if self.head:
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)         
        else :
            self.head = Node(elem)    
        self.size += 1

    def getnode(self,index):   
            pointer = self.head
            for i in range(index):
                if pointer :
                    pointer = pointer.next
                else:
                    raise IndexError('list index out of range')  
            return pointer    
                    

    def __len__(self) :
        return self.size

    def __getitem__(self,index):
              
        pointer = self.getnode(index)
        if pointer :
            return pointer.data
        else:   
            raise IndexError('list index out of range')    

    def __setitem__(self,index,elem):      
            
        pointer = self.getnode(index)
        if pointer :
            pointer.data = elem
        else:   
            raise IndexError('list index out of range')    

    def index(self,elem) :
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == elem : 
                return i 
            pointer = pointer.next
            i = i+1
        raise ValueError(f'{elem} not in the list')    

    def insert(self,index,elem):
        node = Node(elem) 
        if index == 0 :
            node.next = self.head
            self.head = node
        else : 
            pointer = self.getnode(index -1)
            node.next = pointer.next
            pointer.next = node
        self.size += 1    





    def remove(self,elem):
        if self.head == None :
            raise ValueError(f'{elem} not in the list') 
        elif self.head.data == elem :
            self.head = self.head.next
            self.size -= 1
            return True    
        else :
            ancestor = self.head
            pointer = self.head.next    
            while(pointer):
                if pointer.data == elem:
                    ancestor.next = pointer.next
                    pointer.next = None
                    self.size -= 1
                    return True   
                ancestor = pointer
                pointer = pointer.next
        raise ValueError(f'{elem} not in the list')         
 
                 
            
            

    def __repr__(self):
        r = ""
        pointer = self.head
        while(pointer):
            r = r + str(pointer.data) + "->"
            pointer = pointer.next
        return r  

lista = Linkedlist()
# print(len(lista))
lista.append(8)
lista.append(81)
lista.append(88)
lista.append(818)
lista.append(82)
lista.append(810)

lista.remove(8)
lista.remove(88)

print(lista)
# print(len(lista))
# print(lista[0])
# print(lista[1])
# print(lista[2])
# lista.insert(0,55)
# lista.insert(3,99)
# lista.insert(len(lista),1)
#print(lista.index(890))
