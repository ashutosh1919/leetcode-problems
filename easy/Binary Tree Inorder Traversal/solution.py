# Time complexity: O(n)
# Approach: Standard inorder traversal algorithm

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, ans):
        if not root:
            return
        self.inorder(root.left, ans)
        ans.append(root.val)
        self.inorder(root.right, ans)
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.inorder(root, ans)
        return ans