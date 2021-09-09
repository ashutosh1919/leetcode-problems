# Time complexity: O(n)
# Approach: Check following for all node - Absolute Height difference of left and right subtree must be less or equal to 1.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.flag = 0
    
    def checkHeight(self, root, height):
        if not root:
            return height
        lh = self.checkHeight(root.left, height+1)
        rh = self.checkHeight(root.right, height+1)
        if abs(lh-rh)>1:
            self.flag = 1
        return max(lh, rh)
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.checkHeight(root, 0)
        return self.flag==0