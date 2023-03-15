class Node:
    def __init__(self,key):
        self.val = key
        self.right = None
        self.left = None

     def insert(root,key):
        if root is None:
            return Node(key)
        
     else:
        if root.val == key:
        return root
    elif root.val < key:
             root.right = insert(root.right, key)
    else:
         root.left = insert(root.left, key)
    return root
def inorder(root):
     if root:
          inorder(root.left)
          print(root.val, end="")
          inorder(root.right)
            
       


     


    