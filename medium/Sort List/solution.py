# Time complexity: O(nlogn)
# Approach: Merge sort on list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findMid(self, head):
        if not head:
            return head
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, a, b):
        if not a:
            return b
        if not b:
            return a
        res = None
        if a.val<=b.val:
            res = a
            res.next = self.merge(a.next, b)
        else:
            res = b
            res.next = self.merge(a, b.next)
        return res
    
    def mergeSort(self, head):
        if not head or not head.next:
            return head
        mid = self.findMid(head)
        nxt = mid.next
        mid.next = None
        left = self.mergeSort(head)
        right = self.mergeSort(nxt)
        return self.merge(left, right)
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeSort(head)