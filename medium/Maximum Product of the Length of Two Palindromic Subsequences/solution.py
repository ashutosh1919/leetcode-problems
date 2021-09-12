# Time complexity: O(2^n)
# Approach: Use bitmask as subsequence selection and iterate over all subsequences. (https://youtu.be/aoHbYlO8vDg)

class Solution:
    def maxProduct(self, s: str) -> int:
        n, pali = len(s), {}
        for mask in range(1, 1<<n):
            sub = ""
            for i in range(n):
                if mask & (1<<i):
                    sub += s[i]
            if sub == sub[::-1]:
                pali[mask] = len(sub)
        ans = 0
        for m1 in pali:
            for m2 in pali:
                if m1 & m2 == 0:
                    ans = max(ans, pali[m1]*pali[m2])
        return ans