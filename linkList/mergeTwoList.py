class listNode:
    def __init__(self,val):
        self.val = val
        self.next = None

def mergerTwoList(lst1,lst2):
    dummy = listNode(0)
    head = dummy
    while lst1!=None and lst2!=None:
        if lst1.val >= lst2.val:
            dummy.next = lst2
            lst2 = lst2.next
        if lst1.val < lst2.val:
            dummy.next = lst1
            lst1 = lst1.next
        dummy = dummy.next

    if lst1 == None:
        dummy.next = lst2
    if lst2 == None:
        dummy.next = lst1
    return head.next

