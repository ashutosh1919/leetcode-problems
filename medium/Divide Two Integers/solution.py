# Time complexity: O(log(dividend))
# Approach: Divide the dividend by continuously increasing the divisor everytime.

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        minInt, maxInt = -2**31, 2**31-1
        i, sign, ans = 0, (divisor<0) != (dividend<0), 0
        dividend, divisor = abs(dividend), abs(divisor)
        if divisor != 1:
            while divisor<=dividend:
                tmp = divisor
                times = 1
                while dividend >= tmp:
                    dividend -= tmp
                    ans += times
                    tmp += tmp
                    times += times
        else:
            ans = dividend
        if sign:
            ans = max(-2**31, -ans)
        else:
            ans = min(ans, 2**31-1)
        return ans