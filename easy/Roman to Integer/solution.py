# Time complexity: O(len(s))
# Approach: Traverse the roman string from left to right and keep adding the values from mapping.

class Solution:
    def romanToInt(self, s: str) -> int:
        db = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1
        }
        i, ans = 0, 0
        while i < len(s):
            if i+1<len(s):
                if s[i:i+2] in db:
                    ans += db[s[i:i+2]]
                    i += 2
                    continue
            ans += db[s[i]]
            i += 1
        return ans