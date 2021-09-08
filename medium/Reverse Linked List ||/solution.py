# Time complexity: O(n)
# Approach: Keep iterating over list. Whenever left is reached. Do Reverse operation right-left+1 times and attach again to main list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return head
        nHead = ListNode(-501)
        nHead.next = head
        tmp, ct = nHead, 0
        while tmp:
            if ct<left-1:
                tmp = tmp.next
                ct+=1
                continue
            prev, cur, old, nxt = None, tmp.next, tmp.next, None
            tmp.next = None
            times = right-left+1
            for i in range(times):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            tmp.next = prev
            old.next = cur
            break
        return nHead.next