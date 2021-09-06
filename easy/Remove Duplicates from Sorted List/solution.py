# Time complexity: O(n)
# Approach: Two pointer Solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nHead = ListNode(-1)
        nHead.next = head
        tmp, tmp2 = nHead.next, nHead.next
        while tmp and tmp2:
            while tmp and tmp2 and tmp.val==tmp2.val:
                tmp2 = tmp2.next
            tmp.next = tmp2
            tmp = tmp.next
        return nHead.next
        