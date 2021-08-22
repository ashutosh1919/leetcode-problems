# Time complexity: O(log(x))
# Approach: Reversing number logic = ans * 10 + num % 10

class Solution:
    def reverse(self, x: int) -> int:
        intMin, intMax = -(2**31), 2**31 - 1
        sign = -1 if x < 0 else 1
        x = abs(x)
        ans = 0
        while x != 0:
            rem = x % 10
            x //= 10
            if ans > intMax//10 or (ans == intMax//10 and rem>7):
                return 0
            if ans < intMin//10 or (ans == intMin//10 and rem<-8):
                return 0
            ans = ans*10 + rem
            print(ans)
        return ans * sign