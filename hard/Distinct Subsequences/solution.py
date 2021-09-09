# Time complexity: O(m*n)
# Approach: DP Solution (https://www.geeksforgeeks.org/count-distinct-occurrences-as-a-subsequence/)

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(t), len(s)
        if m>n:
            return 0
        dp = [[0]*(n+1) for i in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 0
        for i in range(n+1):
            dp[0][i] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if t[i-1]==s[j-1]:
                    dp[i][j] = dp[i][j-1]+dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[m][n]