# Time complexity: O(m+n)
# Approach: (m+n-1)C(n-1)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path = 1
        for i in range(n, m+n-1):
            path *= i
            path //= (i-n+1)
        return path