# Time complexity: O(n)
# Approach: Choose mid element recursively for each root.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(self, nums, start, end):
        if start>end:
            return None
        mid = (start+end)//2
        node = TreeNode(nums[mid])
        if start==end:
            return node
        node.left = self.build(nums, start, mid-1)
        node.right = self.build(nums, mid+1, end)
        return node
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.build(nums, 0, len(nums)-1)