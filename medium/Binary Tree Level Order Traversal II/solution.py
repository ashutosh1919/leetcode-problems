# Time complexity: O(n)
# Approach: Accumulate numbers in level order traversal in dict but fill the array in reverse order.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, height, mp):
        if not root:
            return height
        if height not in mp:
            mp[height] = [root.val]
        else:
            mp[height].append(root.val)
        h = self.traverse(root.left, height+1, mp)
        h = max(h, self.traverse(root.right, height+1, mp))
        return h
    
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        mp, ans = {}, []
        h = self.traverse(root, 0, mp)
        for i in range(h-1, -1, -1):
            ans.append(mp[i])
        return ans
        