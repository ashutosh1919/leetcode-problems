# Time complexity: O(n*n)
# Approach: Keep swapping the adjust elements on four sides for each layer of matrix.

class Solution:
    def rotate(self, nums: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(nums)
        for i in range(n//2):
            for j in range(i, n-i-1):
                top_left = nums[i][j]
                nums[i][j] = nums[n-j-1][i]
                nums[n-j-1][i] = nums[n-i-1][n-j-1]
                nums[n-i-1][n-j-1] = nums[j][n-i-1]
                nums[j][n-i-1] = top_left
                