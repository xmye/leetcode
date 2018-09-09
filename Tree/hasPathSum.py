def hasPathSum(root,key):
    if root == None:
        return
    if root == key and root.left == None and root.right == None:
        return True
    else:
        return hasPathSum(root.left,key) or hasPathSum(root.right,key)

