# Time complexity: O(n) where n is length of linked list
# Approach: Add numbers digit by digit and add carrry to the next digit sum.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans_node = l1
        carry = 0
        while l1 is not None or l2 is not None or carry:
            l1_val = 0 if l1 is None else l1.val
            l2_val = 0 if l2 is None else l2.val
            s1 = l1_val + l2_val + carry
            s2 = s1 % 10
            carry = s1 // 10;
            if l1 is not None:
                l1.val = s2
                if l1.next is None and (carry != 0 or (l2 is not None and l2.next is not None)):
                    l1.next = ListNode()
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            
        return ans_node
            