# Time complexity: O(m*n)
# Approach: Dynamic programming solution. See the solution on leetcode (https://leetcode.com/problems/interleaving-string/solution/)

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, k = len(s1), len(s2), len(s3)
        if k!=n+m:
            return False
        dp = [[False]*(n+1)]*(m+1)
        for i in range(m+1):
            for j in range(n+1):
                if i==0 and j==0:
                    dp[i][j] = True
                elif i==0:
                    dp[i][j] = dp[i][j-1] and s1[j-1]==s3[i+j-1]
                elif j==0:
                    dp[i][j] = dp[i-1][j] and s2[i-1]==s3[i+j-1]
                else:
                    dp[i][j] = (dp[i][j-1] and s1[j-1]==s3[i+j-1]) or (dp[i-1][j] and s2[i-1]==s3[i+j-1])
        return dp[m][n]
        