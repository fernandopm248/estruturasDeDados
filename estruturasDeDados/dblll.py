from traceback import print_list


class Node :
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None


    def append(self,data) :
        if self.head is None :
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else :
            new_node = Node(data)    
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node    
            new_node.prev = cur
            new_node.next = None

    def prepend(self,data):    
            if self.head is None :
                new_node = Node(data)
                new_node.prev = None
                self.head = new_node    
            else:
                new_node = Node(data) 
                self.head.prev = new_node
                new_node.next = self.head
                self.head = new_node
                new_node.prev = None


    def add_node_after(self,key,data):
        cur = self.head
        while cur :
            if cur.next is None and cur.data == key:
                self.append(data)
                return
            elif cur.data == key:
                new_node = Node(data)  
                nxt = cur.next  
                cur.next = new_node
                new_node.next = nxt
                new_node.prev = cur
                nxt.prev = new_node
            cur = cur.next    
                   

    def add_node_before(self,key,data):
         cur = self.head
         while cur :
            if cur.prev is None and cur.data == key:
                self.prepend(data)
                return
            elif cur.data == key:
                new_node = Node(data)  
                prev = cur.prev
                prev.next = new_node
                cur.prev = new_node
                new_node.next = cur
                new_node.prev = prev
            cur = cur.next    

    def delete(self,key):
        cur = self.head
        while cur :
            if cur.data == key and cur == self.head:
                if not cur.next :
                    cur = None
                    self.head = None
                    return
                else :
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return

            elif cur.data == key :
                if cur.next :
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
                else :
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return    
            cur = cur.next    



    def print_list(self):
        cur = self.head            
        while cur:
            print(cur.data)
            cur = cur.next

a = DoubleLinkedList()
a.append(1)
a.append(2)
a.append(3)
a.append(4)

a.delete(1)
a.delete(3)
a.delete(11)

# a.add_node_before(1,55)
# a.add_node_before(4,34)
a.print_list()