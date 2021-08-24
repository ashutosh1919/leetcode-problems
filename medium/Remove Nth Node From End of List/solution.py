# Time complexity: O(len(LinkedList))
# Approach: Get two pointers and point them to fake node before head. Now, advance fast pointer to n+1 positions. Then while fast is not None, advance slow and fast both. At this point, slow is at one position before then our deletion node.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        fake = ListNode(-1)
        slow, fast = fake, fake
        slow.next, fast.next = head, head
        for i in range(n+1):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return fake.next