# Time complexity: O(m*n)
# Approach: Iterate through the matrix in the given way.

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, n-1, 0, m-1
        ans = []
        ct = m*n
        while left<=right and top<=bottom:
            for i in range(left, right+1):
                ans.append(matrix[top][i])
                ct-=1
            if ct==0:
                break
            for i in range(top+1, bottom+1):
                ans.append(matrix[i][right])
                ct-=1
            if ct==0:
                break
            for i in range(right-1, left-1, -1):
                ans.append(matrix[bottom][i])
                ct-=1
            if ct==0:
                break
            for i in range(bottom-1, top, -1):
                ans.append(matrix[i][left])
                ct-=1
            left, right, top, bottom = left+1, right-1, top+1, bottom-1
        return ans
            