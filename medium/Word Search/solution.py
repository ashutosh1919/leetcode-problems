# Time complexity: O(m*n)
# Approach: DFS traversal from each cell.

class Solution:
    def dfs(self, board, visited, row, col, word, index):
        m, n  = len(board), len(board[0])
        if index == len(word):
            return True
        if board[row][col]!=word[index]:
            return False
        if index == len(word)-1:
            return True
        visited[row][col]=True
        inc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans = False
        for i in inc:
            if row+i[0]<m and row+i[0]>=0 and col+i[1]<n and col+i[1]>=0 and not visited[row+i[0]][col+i[1]]:
                ans |= self.dfs(board, visited, row+i[0], col+i[1], word, index+1)
            if ans:
                break
        visited[row][col]=False
        return ans
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n  = len(board), len(board[0])
        visited = [[False]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if self.dfs(board, visited, i, j, word, 0):
                    return True
        return False