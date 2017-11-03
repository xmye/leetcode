# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None:
            return 
        sumList = ListNode(0)
        head = sumList
        flag = 0
        while   l1  and  l2:
            sumList.val = (l1.val + l2.val + flag)%10
            if (l1.val + l2.val + flag)>=10:
                flag = 1
            else:
                flag = 0
            l1 = l1.next
            l2 = l2.next   
            
            if l1 == None and l2 != None:
                sumList.next = l2
                while flag != 0 and l2 != None:
                    tem = l2.val
                    l2.val =( l2.val + flag)%10
                    if tem + flag >= 10: 
                        flag = 1
                    else:
                        flag = 0
                    l2 = l2.next
                    sumList = sumList.next
                    
            elif l1 != None  and  l2 == None:
                sumList.next = l1
                while flag != 0 and l1 != None:
                    tem = l1.val
                    l1.val =( l1.val + flag)%10
                    if tem + flag >= 10: 
                        flag = 1
                    else:
                        flag = 0
                    l1 = l1.next
                    sumList = sumList.next
                
            if l1 and l2:   
                sumList.next = ListNode(0)
                sumList = sumList.next
            
            if l1 == None and l2 == None and flag != 0:
                sumList.next = ListNode(flag)
                
        return head
        