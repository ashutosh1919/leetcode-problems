# Time complexity: O(n)
# Approach: Accumulate the both ways. At each step, either we can take 2 steps or we can take 1 step excluding the corner cases.

class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2:
            return n
        dp = [0]*n
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n-1]