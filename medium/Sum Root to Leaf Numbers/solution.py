# Time complexity: O(n)
# Approach: Modified preorder traversal with checking leaf node and summing globally.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0
    
    def findSum(self, root, ts):
        if not root:
            return
        if not root.left and not root.right:
            self.sum += int(ts+str(root.val))
            return
        self.findSum(root.left, ts+str(root.val))
        self.findSum(root.right, ts+str(root.val))
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.findSum(root, "")
        return self.sum