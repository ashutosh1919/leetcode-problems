# Time complexity: O(n)
# Approach: Nth Catalan Number = BinomialCoeff of 2nCn divided by (n+1). Tutorial (https://www.geeksforgeeks.org/program-nth-catalan-number/)

class Solution:
    def binCoeff(self, n, k):
        if k>n-k:
            k = n-k
        res = 1
        for i in range(k):
            res *= (n-i)
            res //= (i+1)
        return res
    
    def numTrees(self, n: int) -> int:
        if n<=1:
           return n 
        return self.binCoeff(2*n, n)//(n+1)