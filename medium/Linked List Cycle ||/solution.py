# Time complexity: O(n)
# Approach: Floyd's Cycle detection algorithm.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        slow, fast = head, head
        while slow and fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow==fast:
                break
        if not slow or not fast or not fast.next:
            return None
        slow = head
        while slow!=fast:
            slow, fast = slow.next, fast.next
        return slow