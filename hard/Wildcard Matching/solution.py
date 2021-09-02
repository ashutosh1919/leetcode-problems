# Time complexity: O(len(s)*len(p))
# Approach: Dynamic Programming. (https://www.geeksforgeeks.org/wildcard-pattern-matching/)

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        if m==0:
            return n==0
        dp = [[False]*(m+1) for i in range(n+1)]
        dp[0][0]=True
        for i in range(1, m+1):
            if p[i-1]=='*':
                dp[0][i] = dp[0][i-1]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if p[j-1]=='?' or s[i-1]==p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j] = dp[i][j-1]|dp[i-1][j]
                else:
                    dp[i][j] = False
        return dp[n][m]