# Time complexity: O(n)
# Approach: Floyd's Cycle detection algorithm (https://www.geeksforgeeks.org/detect-loop-in-a-linked-list)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow, fast = head, head
        while slow and fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return True
        return False