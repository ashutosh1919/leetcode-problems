# Time complexity: O(n*(2^n))
# Approach: Backtracking solution to check all partitions.

class Solution:
    def isPal(self, s):
        n = len(s)
        i, j = 0, n-1
        while i<=j:
            if s[i]!=s[j]:
                return False
            i, j = i+1, j-1
        return True
    
    def findPals(self, s, i, tmp, ans):
        if i==len(s):
            ans.append(tmp)
        for k in range(i+1, len(s)+1):
            ts = s[i:k]
            if self.isPal(ts):
                self.findPals(s, k, tmp+[ts], ans)
    
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.findPals(s, 0, [], ans)
        return ans
        