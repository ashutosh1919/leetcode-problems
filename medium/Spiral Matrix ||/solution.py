# Time complexity: O(n*n)
# Approach: Create empty matrix. Iterate through it in spiral way and keep putting the numbers.

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0]*n for i in range(n)]
        num = 1
        left, right, top, bottom = 0, n-1, 0, n-1
        while left<=right and top<=bottom:
            for i in range(left, right+1):
                ans[top][i], num = num, num+1
            if num >= n*n:
                break
            for i in range(top+1, bottom):
                ans[i][right], num = num, num+1
            if num >= n*n:
                break
            for i in range(right, left-1, -1):
                ans[bottom][i], num = num, num+1
            if num >= n*n:
                break
            for i in range(bottom-1, top, -1):
                ans[i][left], num = num, num+1
            left, right, top, bottom = left+1, right-1, top+1, bottom-1
        return ans