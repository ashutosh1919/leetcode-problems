# Time complexity: O(m*n)
# Approach: Find the cells containing O which are not surrounded by Xs using DFS and mark them as A. Mark all other Os as X and mark A containing cells back to O.

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(grid, i, j, m, n):
            if i<0 or j<0 or i>m-1 or j>n-1 or grid[i][j]!='O':
                return 
            grid[i][j] = 'A'
            dfs(grid, i+1, j, m, n)
            dfs(grid, i, j+1, m, n)
            dfs(grid, i-1, j, m, n)
            dfs(grid, i, j-1, m, n)
        
        m, n = len(board), len(board[0])
        if m<=2 or n<=2:
            return
        
        for i in range(m):
            for j in range(n):
                if i==0 or j==0 or i==m-1 or j==n-1:
                    if board[i][j]=='O':
                        dfs(board, i, j, m, n)
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    board[i][j] = 'X'
                if board[i][j]=='A':
                    board[i][j] = 'O'