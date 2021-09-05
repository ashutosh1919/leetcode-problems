# Time complexity: O(m*n*(m+n))
# Approach: Just make all the cells in row and col corresponding to zero to zero except those which are actually zero.

class Solution:
    def makeColRow(self, matrix, row, col, num, m, n):
        for i in range(m):
            if matrix[i][col]!=0:
                matrix[i][col] = num
        for i in range(n):
            if matrix[row][i]!=0:
                matrix[row][i] = num
    
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        maxN = 2**31
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    self.makeColRow(matrix, i, j, maxN, m, n)
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==maxN:
                    matrix[i][j] = 0