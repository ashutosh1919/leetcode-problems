# Time complexity: O(9^3)
# Approach: Brute force solution.

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
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    ans = self.isValid(board, i, j)
                    if not ans:
                        return ans
        return True