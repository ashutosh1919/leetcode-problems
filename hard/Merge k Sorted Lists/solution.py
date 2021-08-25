# Time complexity: O(n*m) where n is list size and m is maximum linked list size
# Approach: Similar as 2 linked lists but here we will have for loop to find minimum.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(-1)
        temp = head
        while True:
            if not any(lists):
                break
            minIndex, minVal = -1, (10**4)+1
            for i in range(len(lists)):
                if lists[i]:
                    if lists[i].val < minVal:
                        minIndex, minVal = i, lists[i].val
            t = lists[minIndex].next
            temp.next = lists[minIndex]
            temp = temp.next
            temp.next = None
            lists[minIndex] = t
        return head.next
        