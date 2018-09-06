import TreeNode
from TreeNode import TreeNode

def treeToDoubleList(root):
    prev = None
    head = None
    treeToDoubleList(root,prev,head)
    return head

def treeToDoubleList(p,prev,head):
    if ~p:
        return
    treeToDoubleList(p.left,prev,head)
    p.left = prev
    if prev:
        head = p
    else:
        prev.right = p
    right = p.left
    # 首尾相连
    head.left = p
    p.right = head
    prev = p
    treeToDoubleList(right,prev,head)

