import listNode
from listNode import listNode
from listNode import g1
from listNode import n1


def addTwoNum(num1,num2):
    flag = 0
    num3 = None
    while num1 != None or num2 != None or flag != 0:
        if num1 == None and num2 != None:
            tmps = num2.val + flag
        if num2 == None and num1 != None:
            tmps = num1.val + flag
        if num1 == None and num2 == None:
            tmps = flag
        if num1 != None and num2 != None:
            tmps = num1.val + num2.val + flag
        if tmps > 9:
            flag = int(tmps / 10)
        else:
            flag = 0
        tmps = tmps % 10
        if num3 == None:
            num3 = listNode(tmps)
            head = num3
        else:
            num3.next = listNode(tmps)
            num3 = num3.next
        if num1 != None:
            num1 = num1.next
        if num2 != None:
            num2 = num2.next
    return head

listNode.printlist(g1)
listNode.printlist(n1)
num3 = addTwoNum(n1,g1)
listNode.printlist(num3)

