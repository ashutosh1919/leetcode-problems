# Time complexity: O(n*n)
# Approach: Recursively build tree (https://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre = 0
    
    def build(self, preorder, inorder, i_start, i_end):
        if i_start > i_end:
            return None
        node = TreeNode(preorder[self.pre])
        self.pre += 1
        if i_start == i_end:
            return node
        index = -1
        for i in range(i_start, i_end+1):
            if inorder[i]==node.val:
                index = i
                break
        node.left = self.build(preorder, inorder, i_start, index-1)
        node.right = self.build(preorder, inorder, index+1, i_end)
        return node
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.build(preorder, inorder, 0, len(inorder)-1)