# Time complexity: O(n)
# Approach: BFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode], height=0) -> int:
        if not root:
            return 0
        def bfs(root, n):
            q, q1 = [root], []
            while q or q1:
                while q:
                    root = q.pop()
                    if not root.left and not root.right:
                        return n
                    if root.left:
                        q1.append(root.left)
                    if root.right:
                        q1.append(root.right)
                n+=1
                q, q1 = q1, []
            return n
        return bfs(root, 1)