class listNode:
    def __init__(self,val):
        self.val = val
        self.next = None

g1 = listNode(3)
g2 = listNode(8)
g3 = listNode(7)
g4 = listNode(1)
g5 = listNode(2)
g6 = listNode(3)
g7 = listNode(4)
g8 = listNode(5)

g1.next = g2
g2.next = g3
g3.next = g4
g4.next = g5
g5.next = g6
g6.next = g7
g7.next = g8
g8.next = g4
