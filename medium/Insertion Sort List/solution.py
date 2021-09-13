# Time complexity: O(n)
# Approach: Same as we do in array. Insert the node in its appropriate position.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findLen(self, head):
        tmp, ct = head, 0
        while tmp:
            ct, tmp = ct+1, tmp.next
        return ct
    
    def swapNodes(self, p1, c1, p2, c2):
        n1, n2 = c1.next, c2.next
        p1.next, c2.next = c2, c1
        p2.next = n2
    
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nhead, ll = None, self.findLen(head)
        if ll==0 or ll==1:
            return head
        dummy = ListNode(-5001, head)
        for i in range(ll):
            prev, tmp, j = dummy, head, 0
            while j<i and tmp:
                if prev.val>tmp.val:
                    break
                prev = tmp
                tmp = tmp.next
                j+=1
            if not tmp:
                continue
            prev2, tmp2 = dummy, dummy.next
            if tmp2.val>tmp.val:
                self.swapNodes(dummy, tmp2, prev, tmp)
                continue
            if prev==dummy:
                continue
            while tmp2 and tmp2!=tmp and tmp2.val<=tmp.val:
                prev2 = tmp2
                tmp2 = tmp2.next
            if tmp2==tmp:
                continue
            self.swapNodes(prev2, tmp2, prev, tmp)
        return dummy.next