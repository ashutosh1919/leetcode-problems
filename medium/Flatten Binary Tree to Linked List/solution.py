# Time complexity: O(n)
# Approach: Recursively flattening. Making left child right child of each node. (https://www.geeksforgeeks.org/flatten-a-binary-tree-into-linked-list/)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root or (not root.left and not root.right):
            return 
        if root.left:
            self.flatten(root.left)
            tmp = root.right
            root.right = root.left
            root.left = None
            
            t = root.right
            while t.right:
                t = t.right
            t.right = tmp
        self.flatten(root.right)