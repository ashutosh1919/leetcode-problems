# Time complexity: O(n^2)
# Approach: Reversing the k-group nodes considering as single linked list and keeping track of previous and next nodes of entire k-group linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def isKNodes(self, head, k):
        tmp = head
        for i in range(k):
            if tmp:
                tmp = tmp.next
            else:
                return False
        return True
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        prv, cur, nxt = None, head, head.next
        gprv, nhead = None, None
        while cur:
            t = cur
            prv = None
            nxt = cur.next
            if not self.isKNodes(t, k):
                if gprv:
                    gprv.next = cur
                else:
                    nhead = cur
                break
            lcur = cur
            for i in range(k):
                nxt = cur.next
                cur.next = prv
                prv = cur
                cur = nxt
            if gprv:
                gprv.next = prv
            if not nhead:
                nhead = prv
            gprv = lcur
        return nhead
            