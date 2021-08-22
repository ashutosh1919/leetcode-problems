# Time complexity: O(mn) where m & n are length of pattern and string
# Approach: Dynamic programming bottom up solution. Please refer this video https://youtu.be/l3hda49XcDE

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        if m == 0:
            return n == 0
        dp = [[False]*(m+1) for i in range(n+1)]
        dp[0][0] = True
        for i in range(1, m+1):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-2]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if p[j-1]=='.' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j] = dp[i][j-2]
                    if p[j-2]=='.' or p[j-2]==s[i-1]:
                        dp[i][j] = dp[i][j] | dp[i-1][j]
                else:
                    dp[i][j] = False
        return dp[n][m]