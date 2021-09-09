# Time complexity: O(n)
# Approach: Summing up triangle from bottom to top in minimum way.

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        for i in range(n-1, 0, -1):
            for j in range(0, len(triangle[i])-1):
                triangle[i-1][j] += min(triangle[i][j], triangle[i][j+1])
        return triangle[0][0]