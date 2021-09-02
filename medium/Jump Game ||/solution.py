# Time complexity: O(n*n)
# Approach: Dynamic Programming (https://www.geeksforgeeks.org/minimum-number-of-jumps-to-reach-end-of-a-given-array/)

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [n+1]*n
        dp[n-1] = 0
        for i in range(n-2, -1, -1):
            for j in range(i+1, min(i+nums[i]+1, n)):
                dp[i] = min(dp[i], dp[j]+1)
        return dp[0]