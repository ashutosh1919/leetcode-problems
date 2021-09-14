# Time complexity: O(n)
# Approach: Find length of both list, advance longer list with extra length and advance both simultaneously.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getLen(self, a):
        tmp, ct = a, 0
        while tmp:
            ct, tmp = ct+1, tmp.next
        return ct
    
    def getIntersectionNode(self, a: ListNode, b: ListNode) -> ListNode:
        la, lb = self.getLen(a), self.getLen(b)
        if la>lb:
            return self.getIntersectionNode(b, a)
        ta, tb = a, b
        for i in range(lb-la):
            tb = tb.next
        while ta!=tb:
            ta, tb = ta.next, tb.next
        return ta