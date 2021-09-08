# Time complexity: O(n) where n is number of nodes in Tree
# Approach: Checking binary search tree conditions on each node recursively.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], l=-2**31-1, r=2**31) -> bool:
        if not root:
            return True
        elif l<root.val and root.val<r:
                return self.isValidBST(root.left, l, root.val) and self.isValidBST(root.right, root.val, r)
        return False