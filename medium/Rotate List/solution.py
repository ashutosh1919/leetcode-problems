# Time complexity: O(n)
# Approach: k=k%n in order to reduce the computation and split list from n-k position and attach tail to head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findLen(self, head):
        tmp, n = head, 0
        while tmp:
            n, tmp = n+1, tmp.next
        return n
            
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        n = self.findLen(head)
        k = k%n
        if k == 0:
            return head
        prev, cur, t = None, head, n-k
        while t:
            t, prev, cur = t-1, cur, cur.next
        tail = cur
        while tail.next:
            tail = tail.next
        prev.next, tail.next = None, head
        return cur