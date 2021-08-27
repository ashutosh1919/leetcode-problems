# Time complexity: O(len(haystack)+len(needle))
# Approach: Knuth Morris Pratt (KMP) Algorithm

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if n == 0:
            return 0 if m==0 else -1
        if m==0:
            return 0
        i, j = 1, 0
        kmp = [0]*m
        while i<m:
            if needle[i]==needle[j]:
                kmp[i] = j+1
                i+=1
                j+=1
            else:
                if j!=0:
                    j = kmp[j-1]
                else:
                    kmp[i] = 0
                    i += 1
        i, j = 0, 0
        while i<n:
            if haystack[i]==needle[j]:
                i+=1
                j+=1
            if j==m:
                return i-j
            elif i<n and haystack[i]!=needle[j]:
                if j!=0:
                    j = kmp[j-1]
                else:
                    i+=1
        return -1
            