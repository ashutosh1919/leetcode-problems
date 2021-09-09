# Time complexity: O(n*n)
# Approach: Traverse tree recursively and build. Similar as preorder and inorder but here we need to build right subtree first.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.post = 0
    
    def build(self, postorder, inorder, i_start, i_end):
        if i_start > i_end:
            return None
        node = TreeNode(postorder[self.post])
        self.post -= 1
        if i_start == i_end:
            return node
        index = -1
        for i in range(i_start, i_end+1):
            if inorder[i]==node.val:
                index = i
                break
        node.right = self.build(postorder, inorder, index+1, i_end)
        node.left = self.build(postorder, inorder, i_start, index-1)
        return node
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.post = len(postorder)-1
        return self.build(postorder, inorder, 0, len(inorder)-1)