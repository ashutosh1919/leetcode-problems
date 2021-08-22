# Time complexity: O(n)
# Approach: Reading the string as if we are traversing it in zigzag. Note that solution without using memory is little bit tricky. So, you can use empty array of strings and then problem becomes easy. Just store string in 2D array and read in zigzag.

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        cycle = 2*(numRows-1)
        i, j, ans = 0, 0, ""
        while i<numRows:
            j = 0
            while i+j < len(s):
                ans += s[i+j]
                if i != 0 and i != numRows-1 and (j+cycle-i)<len(s):
                    ans += s[j+cycle-i]
                j += cycle
            i += 1
        return ans
            