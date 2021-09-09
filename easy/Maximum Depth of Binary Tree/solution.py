# Time complexity: O(n)
# Approach: Recursive traversal with accumulating depth.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode], height=0) -> int:
        if not root:
            return height
        h = self.maxDepth(root.left, height+1)
        h = max(h, self.maxDepth(root.right, height+1))
        return h