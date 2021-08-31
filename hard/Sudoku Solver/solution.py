# Time complexity: O(9^(n*n))
# Approach: Backtracking the solution. (https://www.geeksforgeeks.org/sudoku-backtracking-7/)

class Solution:
    def isValid(self, board, row, col):
        for i in range(9):
            if col!=i and board[row][i]==board[row][col]:
                return False
        for i in range(9):
            if row!=i and board[i][col]==board[row][col]:
                return False
        gridX, gridY = col//3, row//3
        for i in range(gridX*3, gridX*3+3):
            for j in range(gridY*3, gridY*3+3):
                if (i!=col or j!=row) and board[row][col]==board[j][i]:
                    return False
        return True
        
    def backTrack(self, board, row, col):
        if row==8 and col==9:
            return True
        if col==9:
            row += 1
            col = 0
        if board[row][col]!='.':
            return self.backTrack(board, row, col+1)
        for i in range(1, 10):
            board[row][col] = str(i)
            if self.isValid(board, row, col):
                if self.backTrack(board, row, col+1):
                    return True
            board[row][col] = '.'
        return False
        
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backTrack(board, 0, 0)
        