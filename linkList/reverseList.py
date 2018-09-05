from listNode import listNode
from listNode import g1

def reverseList(lst):
    if lst == None or lst.next == None:
        return lst
    first = None
    sceond = lst
    third = lst.next
    while third.next != None:
        sceond.next = first
        first = sceond
        sceond = third
        third = third.next
    sceond.next = first
    third.next = sceond
    return third

node = g1
nodelist = []
while node!= None:
    nodelist.append(node.val)
    node = node.next
print("init list:",nodelist)

res = []
reverseNode = reverseList(g1)
while reverseNode!= None:
    res.append(reverseNode.val)
    reverseNode = reverseNode.next
print("reverse node:",res)
