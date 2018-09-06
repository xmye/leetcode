import listNode
from listNode import listNode
from listNode import g1

def partitionLinklist(lst,k):
    dummy = listNode(0)
    partition = listNode(k)
    first,second,cur = dummy,partition,lst
    while cur != None:
        next = cur.next
        if cur.val <= k:
            first.next = cur
            first = cur
        if cur.val > k:
            second.next = cur
            second = cur
        cur = next
    first.next = partition.next
    return dummy.next

listNode.printlist(g1)
partition = partitionLinklist(g1,4)
listNode.printlist(partition)