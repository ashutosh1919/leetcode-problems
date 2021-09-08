# Time complexity: O(n)
# Approach: Recursive or iterative (both will work) with memoization.

class Solution:
    def __init__(self):
        self.memoize = {}
        
    def findSolutions(self, s, i, mp):
        if i>=len(s):
            return 1
        ans = 0
        if s[i] in mp:
            if i+1 in self.memoize:
                ans += self.memoize[i+1]
            else:
                ans += self.findSolutions(s, i+1, mp)
        if i+1<len(s) and s[i:i+2] in mp:
            if i+2 in self.memoize:
                ans += self.memoize[i+2]
            else:
                ans += self.findSolutions(s, i+2, mp)
        self.memoize[i] = ans
        return ans
    
    def numDecodings(self, s: str) -> int:
        mp = {}
        for i in range(26):
            mp[str(i+1)] = chr(ord('A')+i)
        return self.findSolutions(s, 0, mp)