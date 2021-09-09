# Time complexity: O(n*n)
# Approach: store list in array and then generate.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
    
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return self.build(nums, 0, len(nums)-1)