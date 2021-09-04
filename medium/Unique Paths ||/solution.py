# Time complexity: O(m*n)
# Approach: Bottom up DP solution using same grid (https://www.geeksforgeeks.org/unique-paths-in-a-grid-with-obstacles/)

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[0][0]:
            return 0
        grid[0][0]=1
        for i in range(1, n):
            grid[0][i] = 0 if grid[0][i]==1 else grid[0][i-1]
        
        for i in range(1, m):
            grid[i][0] = 0 if grid[i][0]==1 else grid[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = 0 if grid[i][j]==1 else grid[i-1][j]+grid[i][j-1]
        return grid[m-1][n-1]