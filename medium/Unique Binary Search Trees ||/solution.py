# Definition for a binary tree node.
# class TreeNode:
# Time complexity: O(C0+C1+...Cn), where Cn is the Catalan number
# Approach: Pick any number as root. Left side elements will lie in left subtree and right side elements will lie on right subtree.

#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dfs(left, right):
            if left>right:
                return [None]
            if left==right:
                return [TreeNode(left)]
            ans = []
            for i in range(left, right+1):
                leftNode = dfs(left, i-1)
                rightNode = dfs(i+1, right)
                for l in leftNode:
                    for r in rightNode:
                        root = TreeNode(i, l, r)
                        ans.append(root)
            return ans
        return dfs(1, n)