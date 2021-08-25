# Time complexity: O(2^(2n))
# Approach: Simple recursion solves the problem. We need to make sure that whenever we want to insert closing bracket, then number opening brackets must be less than number of closing brackets.

class Solution:
    def stringGenerator(self, i, j, rem, ans):
        if i == 0 and j == 0:
            ans.append(rem)
            return
        if i != 0:
            self.stringGenerator(i-1, j, rem + "(", ans)
        if j != 0 and i<j:
            self.stringGenerator(i, j-1, rem + ")", ans)
        
    
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        if n == 0:
            return ans
        self.stringGenerator(n, n, "", ans)
        return ans