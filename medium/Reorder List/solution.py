# Time complexity: O(n)
# Approach: Find mid and partition the list from mid, reverse the right half and merge.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findMid(self, head):
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverseList(self, head):
        prev, cur, nxt = None, head, head.next
        while nxt:
            cur.next = prev
            prev = cur
            cur = nxt
            nxt = cur.next
        cur.next = prev
        return cur
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        mid = self.findMid(head)
        head2 = self.reverseList(mid.next)
        mid.next = None
        fl, sl = head, head2
        while fl and sl:
            flt, slt = fl.next, sl.next
            fl.next = sl
            sl.next = flt
            fl = flt
            sl = slt
        return head