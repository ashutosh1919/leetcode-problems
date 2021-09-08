# Time complexity: O(n) where n is number of nodes
# Approach: Inorder traversal and swapping of node values. (https://www.geeksforgeeks.org/fix-two-swapped-nodes-of-bst/)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstUtil(self, root, first, mid, last, prev):
        if root:
            self.bstUtil(root.left, first, mid, last, prev)
            if prev[0] and root.val<prev[0].val:
                if not first[0]:
                    first[0], mid[0] = prev[0], root
                else:
                    last[0] = root
            prev[0] = root
            self.bstUtil(root.right, first, mid, last, prev)
    
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first, mid, last, prev = [None], [None], [None], [None]
        self.bstUtil(root, first, mid, last, prev)
        if first[0] and last[0]:
            first[0].val, last[0].val = last[0].val, first[0].val
        elif first[0] and mid[0]:
            first[0].val, mid[0].val = mid[0].val, first[0].val