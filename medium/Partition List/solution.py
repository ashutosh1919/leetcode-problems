# Time complexity: O(n)
# Approach: Two pointers (<x, >=x) to store information and join them.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        sm1, sm2, bg1, bg2 = None, None, None, None
        tmp = head
        while tmp:
            if tmp.val<x:
                if not sm1:
                    sm1=sm2=tmp
                else:
                    sm2.next = tmp
                    sm2 = sm2.next
            else:
                if not bg1:
                    bg1=bg2=tmp
                else:
                    bg2.next = tmp
                    bg2 = bg2.next
            tmp = tmp.next
        if bg2:
            bg2.next = None
        if not sm1:
            return bg1
        sm2.next = bg1
        return sm1