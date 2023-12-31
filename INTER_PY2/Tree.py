class Node:   
    def __init__(self,val):  
        self.lc=None
        self.rc=None
        self.nodedata = val
        
root = Node(1)
root.lc = Node(2)
root.rc = Node(3)
root.lc.lc = Node(4)
root.lc.rc = Node(5)

# Inorder
def Inorder(root):  
    if root:    
        Inorder(root.lc)
        print (root.nodedata)
        Inorder(root.rc)
        
Inorder(root)
print("--------------")
# Postorder
def Postorder(root):  
    if root:    
        Inorder(root.lc)
        Postorder(root.rc)
        print (root.nodedata)
        
Postorder(root)
print("--------------")
# Postorder
def Preorder(root):  
    if root:    
        print(root.nodedata)
        Preorder (root.lc)
        Preorder(root.rc)
        
Preorder(root)