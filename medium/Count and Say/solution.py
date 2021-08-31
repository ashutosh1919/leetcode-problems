# Time complexity: O(n*n)
# Approach: Recreating ans string again and again for n-1 times.

class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"
        for i in range(1, n):
            tmp, cop = "", ans
            i, j = 0, 0
            while i< len(cop):
                j = i
                while j < len(cop) and cop[i]==cop[j]:
                    j+=1
                ct = j-i
                tmp += str(ct)+cop[i]
                i = j
            ans = tmp
        return ans