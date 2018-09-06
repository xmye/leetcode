
class TreeNode:

    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None


root = TreeNode(5)
root.left = 3
root.right = 7
root.left.left = 1
root.left.right = 4
root.right.right = 9
