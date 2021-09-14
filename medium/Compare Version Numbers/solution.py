# Time complexity: O(n)
# Approach: Version by version comparison.

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        n, m = len(version1), len(version2)
        i, j = 0, 0
        while i< n or j<m:
            s1, s2 = 0, 0
            while i<n and version1[i]!='.':
                s1 = s1*10 + int(version1[i])
                i+=1
            i+=1
            while j<m and version2[j]!='.':
                s2 = s2*10 + int(version2[j])
                j+=1
            j+=1
            # print(s1, s2)
            if s1>s2:
                return 1
            elif s1<s2:
                return -1
        return 0