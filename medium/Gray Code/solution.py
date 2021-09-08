# Time complexity: O(n*2^n)
# Approach: n bit gray code is generated using n-1 bit gray code.

class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans, rest = [0], [1]
        j = 0
        while j < n:
            for i in range(2**j-1):
                diff = ans[i+1]-ans[i]
                rest.append(rest[i]+diff)
            rest.reverse()
            ans.extend(rest)
            j+=1
            rest = [2**j]
        return ans