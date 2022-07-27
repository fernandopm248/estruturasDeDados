from pickle import NONE
from tkinter.messagebox import NO


class Node :
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


        def __str__(self):
            return str(self.data)

class BinaryTree:     
     def __init__(self,data=None):
         if data:
            node = Node(data)   
            self.root = node
         else :
             self.root = None  


     def simetric_traversal(self,node=None):     

         if node is None :
          node = self.root 
         if node.left:
          print('(',end='')
          self.simetric_traversal(node.left)     
         print(node.data,end='')     
         if node.right:
         
          self.simetric_traversal(node.right)
          print(')',end='')  

     def postorder_traversal(self,node=None) :
         if node is None:
             node = self.root
         if node.left:
             self.postorder_traversal(node.left)
         if node.right:
              self.postorder_traversal(node.right)
         print(node.data)     

     def height(self,node=None) :
        if node is None:
             node = self.root
        hleft = 0
        hright = 0     
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        if hright > hleft :
            return hright + 1
        return hleft + 1        
           


        


        #   '+'
        #    /     \
#  'a'      '*'
#          /   \
#        'b'    '-'
#              /    \
#            '/'    'e' 
#           /   \
#         'c'   'd'

#(a + (b * ((c/d) - e)))



# tree = BinaryTree()
# n1 = Node('a')
# n2 = Node('+')
# n3 = Node('*')
# n4 = Node('b')
# n5 = Node('-')
# n6 = Node('/')
# n7 = Node('c')
# n8 = Node('d')
# n9 = Node('e')

# n6.left = n7
# n6.right = n8
# n5.left = n6
# n5.right = n9
# n3.left = n4
# n3.right = n5
# n2.left = n1
# n2.right = n3

# tree.root = n2
# tree.simetric_traversal()
# print('')  

def postorder_example_tree():
    tree = BinaryTree()
    n1 = Node('I')
    n2 = Node('N')
    n3 = Node('S')
    n4 = Node('C')
    n5 = Node('R')
    n6 = Node('E')
    n7 = Node('V')
    n8 = Node('A')
    n9 = Node('5')
    n0 = Node('3')

    n0.left = n6
    n0.right = n9
    n6.left = n1
    n6.right = n5
    n5.left = n2
    n5.right = n4
    n4.right = n3
    n9.left = n8
    n8.right = n7

    tree.root = n0
    return tree


if __name__ == "__main__":
    tree = postorder_example_tree()
    print("Percurso em pós ordem:")
    # tree.postorder_traversal()
    print(tree.height())
   



# tree = BinaryTree(25)
# tree.root.left = Node(50)    
# tree.root.right = Node(75)

# print(tree.root.data) 
# print(tree.root.left.data) 
# print(tree.root.right.data) 