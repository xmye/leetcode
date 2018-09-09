import TreeNode
from TreeNode import TreeNode
import Queue

# 二叉搜索树中的最小公共节点 左>中>右
def LCA(root,p,q):
    if root == None or p == None or q == None:
        return
    if root.val > p.val and root.val > q.val:
        return LCA(root.left,p,q)
    elif root.val < p.val and root.val < q.val:
        return LCA(root.right,p,q)
    else:
        return root

# 二叉树中搜索最小公共节点,节点存取其父节点
def LCA2(root,p,q):
    if root == None or p == None or q == None:
        return
    pq = TreeNode(0)
    findNode(root,p,q,pq)
    pp = pq.left
    qq = pq.left
    if pp == None or qq == None:
        return
    lenp,lenq = 0,0
    up1,up2 = pp,qq
    while up1 != root:
        up1 = up1.partent
        lenp += 1
    while up2 != root:
        up2 = up2.parent
        lenq += 1
    up1,up2 = pp,qq

    while lenp > lenq:
        up1 = up1.parent
        lenp -= 1
    while lenp < lenq:
        up2 = up2.parent
        lenq -= 1

    while up1 != up2:
        up1 = up1.parent
        up2 = up2.parent

    return up1

# 二叉树中搜索最小公共节点
def LCA3(root,p,q):
    if root == None or p == None or q == None:
        return
    if root == p or root == q:
        return root
    left = LCA3(root.left,p,q)
    right = LCA3(root.right,p,q)
    if left != None and right != None:
        return root
    if left == None and right != None:
        return right
    if right == None and left != None:
        return left

def LCA4(root,p,q):
    if root == None or p == None or q == None:
        return
    currLevel,nextLevel = Queue(),Queue()
    currLevel.put(root)
    backTracking = dict()
    pp,qq = Queue(),Queue()





def findNode(root,p,q,pq):
    if root == None:
        return
    if root == p:
        pq.left = root
    if root == q:
        pq.left = root
    if pq.left == None or pq.right == None:
        findNode(root.left,p,q,pq)
        findNode(root.right,p,q,pq)



