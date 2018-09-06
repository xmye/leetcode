

def LCA(root,p,q):
    if root == None or p == None or q == None:
        return
    if root.val > p.val and root.val > q.val:
        return LCA(root.left,p,q)
    elif root.val < p.val and root.val < q.val:
        return LCA(root.right,p,q)
    else:
        return root

