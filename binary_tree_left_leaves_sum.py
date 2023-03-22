class Node:
    def __init__(self, data, left=None, right=None):
        self.left=left
        self.right=right
        self.data=data

def isLeaf(data):
    if data is None:
        return False
    if data.left is None and data.right is None:
        return True
    return False

def left_leaves_sum(root):
    res = 0
        
    # Update result if root is not None
    if root is not None:

        # If left of root is None, then add key of
        # left child
        if isLeaf(root.left):
            res += root.left.data
        else:
            # Else recur for left child of root
            res += left_leaves_sum(root.left)

        # Recur for right child of root and update res
        res += left_leaves_sum(root.right)
    return res
        
    
    
if __name__=="__main__":

    root=Node(3)
    root.left=Node(9)
    root.right=Node(20)
    root.right.left=Node(15)
    root.right.right=Node(7)
    print(left_leaves_sum(root))
