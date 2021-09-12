# Time complexity: O(n)
# Approach: Store mapping of nodes in dict and then point to the next and random.

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        mp, tmp = {}, head
        while tmp:
            mp[tmp] = Node(tmp.val)
            tmp = tmp.next
        tmp = head
        while tmp:
            if tmp.next:
                mp[tmp].next = mp[tmp.next]
            if tmp.random:
                mp[tmp].random = mp[tmp.random]
            tmp = tmp.next
        return mp[head]