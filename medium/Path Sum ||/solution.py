# Time complexity: O(n)
# Approach: Reducing path sum and adding root value in temporary array. Recursively doing this for all.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findPaths(self, root, targetSum, tmp, ans):
        if not root:
            return
        if not root.left and not root.right:
            if targetSum==root.val:
                ans.append(tmp+[root.val])
            return
        if root.left:
            self.findPaths(root.left, targetSum-root.val, tmp+[root.val], ans)
        if root.right:
            self.findPaths(root.right, targetSum-root.val, tmp+[root.val], ans)
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        self.findPaths(root, targetSum, [], ans)
        return ans