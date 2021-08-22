# Time complexity: O(log10(x))
# Approach: Reverse the number and check if it is same as original number.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x == -2**31:
            return False
        dup, ans = x, 0
        while dup!=0:
            ans = ans*10 + dup%10
            dup //= 10
        return ans == x