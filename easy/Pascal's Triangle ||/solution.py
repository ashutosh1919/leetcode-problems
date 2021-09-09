# Time complexity: O(n*n)
# Approach: Use binomial formula to create only required row.

class Solution:
    def nCk(self, n, k):
        if k==0 or k==n:
            return 1
        if k>n-k:
            k=n-k
        res = 1
        for i in range(k):
            res *= (n-i)
            res //= (i+1)
        return res
    
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        for i in range(rowIndex+1):
            ans.append(self.nCk(rowIndex, i))
        return ans