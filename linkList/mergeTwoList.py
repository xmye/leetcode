from listNode import listNode

def mergerTwoList(lst1,lst2):
    dummy = listNode(0)
    head = dummy
    while lst1!=None and lst2!=None:
        if lst1.val > lst2.val:
            dummy.next = lst2
            lst2 = lst2.next
        if lst1.val <= lst2.val:
            dummy.next = lst1
            lst1 = lst1.next
        dummy = dummy.next

    if lst1 == None:
        dummy.next = lst2
    if lst2 == None:
        dummy.next = lst1
    return head.next


# test
n1 = listNode(5)
n2 = listNode(15)
n3 = listNode(10)
n4 = listNode(15)
n5 = listNode(20)

n1.next = n2
n3.next = n4
n4.next = n5

print("init list:",n1,n3)
res = mergerTwoList(n1,n3)
while res != None:
    print("result list:",res.val)
    res = res.next
