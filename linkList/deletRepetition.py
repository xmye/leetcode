import listNode
from listNode import listNode
from listNode import n1

def deletRepetition(lst):
    pre = listNode(lst.val)
    head = pre
    cur = lst
    while cur != None:
        if pre.val != cur.val:
            pre.next = listNode(cur.val)
            pre = pre.next
        cur = cur.next

    return head

# 删除所有重复节点
def deletAllRepetition(lst):
    dummy = listNode(0)
    tail = dummy
    pre,cur = lst,lst
    while cur != None and cur.next != None:
        while cur.next != None and cur.val == cur.next.val:
            cur = cur.next
        if pre == cur: # 节点未重复
            tail.next = pre
            tail = tail.next
        cur = cur.next
        pre = cur
    tail.next = cur
    return dummy.next

listNode.printlist(n1)
n2 = deletRepetition(n1)
listNode.printlist(n2)
n3 = deletAllRepetition(n1)
listNode.printlist(n3)
