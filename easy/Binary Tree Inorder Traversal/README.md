Given the `root` of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
![Example_1_img](https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg)
```
Input: root = [1,null,2,3]
Output: [1,3,2]
```
Example 2:
```
Input: root = []
Output: []
```
Example 3:
```
Input: root = [1]
Output: [1]
```
Example 4:
![Example_2_img](https://assets.leetcode.com/uploads/2020/09/15/inorder_5.jpg)
```
Input: root = [1,2]
Output: [2,1]
```
Example 5:
![Example_3_img](https://assets.leetcode.com/uploads/2020/09/15/inorder_4.jpg)
```
Input: root = [1,null,2]
Output: [1,2]
```

Constraints:
- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

**Follow up**: Recursive solution is trivial, could you do it iteratively?
