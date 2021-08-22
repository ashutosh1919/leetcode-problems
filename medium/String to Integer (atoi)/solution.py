# Time complexity: O(len(s))
# Approach: Implemented the rules described as it is.

class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        intMin, intMax = -2**31, 2**31-1
        i, sign, ans = 0, 1, 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            if s[i] not in ['-', '+'] and (ord(s[i]) < ord('0') or ord(s[i]) > ord('9')):
                return 0
            if s[i] == '-':
                i += 1
                sign = -1
            elif s[i] == '+':
                i += 1
                sign = 1
            if i<len(s) and (ord(s[i])<ord('0') or ord(s[i])>ord('9')):
                return 0
            if i >= len(s):
                return 0
            while i<len(s) and s[i]=='0':
                i += 1
            if i >= len(s):
                return 0
            while i<len(s) and ord(s[i])>=ord('0') and ord(s[i])<=ord('9'):
                if sign == -1 and (ans > intMax//10 or (ans == intMax//10 and int(s[i])>8)):
                    return intMin
                elif sign == 1 and (ans > intMax//10 or (ans == intMax//10 and int(s[i])>7)):
                    return intMax
                ans = ans*10 + int(s[i])
                i += 1
            break
        return ans * sign
            