from traceback import print_list


class Node :
    def __init__(self,data):
        self.data = data
        self.next = None
  

class CircularLinkedList:
    def __init__(self):
        self.head = None


    def append(self,data) :
      if not self.head:
          self.head = Node(data)
          self.head.next = self.head
      else:
        new_node = Node(data)
        cur = self.head
        while cur.next != self.head :
            cur = cur.next
        cur.next = new_node
        new_node.next = self.head


    def prepend(self,data):    
          new_node = Node(data)
          cur = self.head
          new_node.next = self.head

          if not self.head :
              new_node.next = new_node
          else :
              while cur.next != self.head:
                  cur = cur.next
              cur.next = new_node       
          self.head = new_node  

    def remove(self,key):
        if self.head.data == key :
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next  
        else :
            cur = self.head
            prev = None
            while cur.next != self.head :
                prev = cur
                cur = cur.next
                if cur.data == key:
                    prev.next = cur.next
                    cur = cur.next      



    def print_list(self):
        cur = self.head            
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head : break

a = CircularLinkedList()
a.append(1)
a.append(22)
a.append(33)
a.append(44)
a.append(1115)
a.prepend(25)
a.remove(25)
a.remove(44)
a.remove(1115)
a.remove(56)
a.print_list()