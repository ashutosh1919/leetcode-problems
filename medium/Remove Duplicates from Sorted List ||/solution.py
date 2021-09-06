# Time complexity: O(n)
# Approach: Two pointer solution with added dummy node on the head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nHead = ListNode(-1)
        nHead.next = head
        tmp, tmp2 = nHead, nHead.next
        while tmp and tmp2:
            fl = 0
            while tmp2 and tmp2.next and tmp2.val==tmp2.next.val:
                tmp2 = tmp2.next
                fl = 1
            if not fl:
                tmp.next = tmp2
                tmp = tmp.next
            tmp2 = tmp2.next
        if tmp:
            tmp.next = None
        return nHead.next
                
        