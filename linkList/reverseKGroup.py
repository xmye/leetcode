from listNode import listNode
from listNode import g1

def reverseKGroup(lst,k):
    if lst == None or k <= 1:
        return
    dummy = listNode(0)
    dummy.next = lst
    pre = dummy
    cross = lst
    count = 0
    while cross != None:
        count += 1
        if count % k == 0:
            pre = reverse(pre,cross.next)
            cross.next = pre
        else:
            cross.next = cross
    return dummy.next

def reverse(pre,end):
    last = pre.next
    cur = last.next
    while cur != end:
        last.next = cur.next
        cur.next = pre.next
        pre.next = cur
        cur = last.next
    return last

def reverseList(pre,end):
    lst = pre.next
    first = pre
    sceond = lst
    third = lst.next
    while third != end:
        sceond.next = first
        first = sceond
        sceond = third
        third = third.next
    sceond.next = first
    third.next = sceond
    return lst

node = g1
nodelist = []
while node!= None:
    nodelist.append(node.val)
    node = node.next
print("init list:",nodelist)

res = []
reverseNode = reverseKGroup(g1,2)
while reverseNode!= None:
    res.append(reverseNode.val)
    reverseNode = reverseNode.next
print("reverse node:",res)
