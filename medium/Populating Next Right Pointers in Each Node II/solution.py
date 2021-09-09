# Time complexity: O(n)
# Approach: Recursively handling null conditions.

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def findChildNext(self, root):
        while root:
            if root.left:
                return root.left
            if root.right:
                return root.right
            root = root.next
        return None
    
    def populateNext(self, root):
        if not root:
            return
        if not root.left and not root.right:
            return
        nxtChild = self.findChildNext(root.next)
        if root.left and root.right:
            root.left.next = root.right
            root.right.next = nxtChild
        elif root.left:
            root.left.next = nxtChild
        elif root.right:
            root.right.next = nxtChild
        self.populateNext(root.right)
        self.populateNext(root.left)
    
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        root.next = None
        self.populateNext(root)
        return root