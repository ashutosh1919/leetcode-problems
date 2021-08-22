# Time complexity: O(log10(num))
# Approach: Keep dividing from biggest to smallest number.

class Solution:
    def intToRoman(self, num: int) -> str:
        db = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        ans = ""
        while num != 0:
            for div in db:
                r = num // div[0]
                if r!=0:
                    ans += div[1]*r
                    num = num % div[0]
        return ans
        