from listNode import listNode
from listNode import g1

def getCirleLength(lst):
    slow = lst
    if slow == None or slow.next == None:
        return 0
    fast = slow.next.next
    while fast != None and fast.next != None:
        if slow == fast :
            return getLength(slow)
        slow = slow.next
        fast = fast.next.next
    return 0

def getLength(node):
    curr = node
    count = 1
    while curr.next != node:
        curr = curr.next
        count += 1
    return count


print("init list:",g1)
print("getCirleLength",getCirleLength(g1))


