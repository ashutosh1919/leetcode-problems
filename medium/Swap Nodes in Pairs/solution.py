# Time complexity: O(len(list))
# Approach: Add dummy node before the linked list and keep swapping elements in pairs of 2.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        temp = ListNode(-1)
        temp.next = head
        ans = temp
        while temp.next:
            a = temp.next
            b = temp.next.next
            if not b:
                break
            bN = b.next
            temp.next = b
            b.next = a
            a.next = bN
            temp = a
        return ans.next