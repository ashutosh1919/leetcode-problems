# Time complexity: O(n)
# Approach: Straight forward joining.

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
    def populateNext(self, root):
        if not root.left:
            return
        if root.left:
            root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        else:
            root.right.next = None
        self.populateNext(root.left)
        self.populateNext(root.right)
    
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        root.next = None
        self.populateNext(root)
        return root