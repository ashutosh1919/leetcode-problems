# Time complexity: O(n!)
# Approach: Backtracking

class Solution:
    def isValidCell(self, grid, row, col):
        n = len(grid)
        for i in range(n):
            if row!=i and grid[i][col]=='Q':
                return False
            if col!=i and grid[row][i]=='Q':
                return False
        k, l = row-1, col-1
        while k>=0 and l>=0:
            if grid[k][l]=='Q':
                return False
            k=k-1
            l=l-1
        k, l = row+1, col+1
        while k<n and l<n:
            # print(k, l)
            if grid[k][l]=='Q':
                return False
            k = k + 1
            l = l + 1
        k, l = row+1, col-1
        while k<n and l>=0:
            if grid[k][l]=='Q':
                return False
            k=k+1
            l=l-1
        k, l = row-1, col+1
        while k>=0 and l<n:
            if grid[k][l]=='Q':
                return False
            k=k-1
            l=l+1
        return True
    
    def isValidGrid(self, grid):
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j]=='Q' and not self.isValidCell(grid, i, j):
                    return False
        return True
    
    def backTrack(self, row, grid, ans):
        n = len(grid)
        if row>=n:
            return ans
        for i in range(n):
            grid[row][i]='Q'
            if self.isValidGrid(grid):
                if row==n-1:
                    ans+=1
                else:
                    ans = self.backTrack(row+1, grid, ans)
            grid[row][i]='.'
        return ans
    
    def totalNQueens(self, n: int) -> int:
        grid = [["."]*n for i in range(n)]
        return self.backTrack(0, grid, 0)