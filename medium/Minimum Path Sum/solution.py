# Time complexity: O(m*n)
# Approach: DP solution. Accumulating minimum sum

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[101]*n for i in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, n):
            dp[0][i] = dp[0][i-1]+grid[0][i]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0]+grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1])+grid[i][j]
        return dp[m-1][n-1]
            