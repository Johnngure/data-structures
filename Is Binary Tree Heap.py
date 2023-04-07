class Solution:
    def size_bt(self, node):
        if node is None:
            return 0
        else:
            return (self.size_bt(node.left) + 1 + self.size_bt(node.right))    
    
    def isValid(self, root, level ,n):
        if root is None:
            return True
        if level >= n:
            return False
        return self.isValid(root.right, 2*level+2, n) and self.isValid(root.left, 2*level+1, n)
    
    def propHolder(self, root):
        if not root.left and not root.right:
            return True
        if root.right is None:
            return root.data > root.left.data
        else:
            if root.data >= root.left.data and root.data >= root.right.data:
                return self.propHolder(root.left) and self.propHolder(root.right)
            else:
                return False

    #Your Function Should return True/False or 1/0
    def isHeap(self, root):
        #Code Here
        if root is None:
            return True
        noOfNodes = self.size_bt(root)
        return self.isValid(root, 0, noOfNodes) and self.propHolder(root)