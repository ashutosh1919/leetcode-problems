# Time complexity: O(n)
# Approach: Left & Right Traversal to check the max length. We are not using any additional memory but it can also be done using stack. All solutions are explained here: https://www.geeksforgeeks.org/length-of-the-longest-valid-substring/

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n in [0, 1]:
            return 0
        left, right, mxLen = 0, 0, 0
        for i in range(n):
            if s[i]=='(':
                left+=1
            else:
                right+=1
            if left==right:
                mxLen = max(mxLen, 2*right)
            elif right>left:
                left, right = 0, 0
        left, right = 0, 0
        for i in range(n-1, 0, -1):
            if s[i]=='(':
                left+=1
            else:
                right+=1
            if left==right:
                mxLen = max(mxLen, 2*left)
            elif left>right:
                left, right = 0, 0
        return mxLen