# Time complexity: O(len(l1)+len(l2))
# Approach: Consider l1 as base and we will create final list in l1. We need to insert node from l2 into l1 only if (l1.val <= l2.val and l1.next.val >= l2.val).

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doMergeOp(self, small, large, smallNext):
        small.next = large
        largeNext = large.next
        large.next = smallNext
        return largeNext
    
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val > l2.val:
            return self.mergeTwoLists(l2, l1)
        ans = l1
        while l1.next and l2:
            if l1.val <= l2.val and l1.next.val >= l2.val:
                l2 = self.doMergeOp(l1, l2, l1.next)
                l1 = l1.next
            else:
                l1 = l1.next
        if l2:
            l1.next = l2
        return ans