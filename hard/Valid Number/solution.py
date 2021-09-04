# Time complexity: O(n):
# Approach: Implementing whatever mentioned about Decimal and Integers.

class Solution:
    def isNumber(self, s: str) -> bool:
        i, n = 0, len(s)
        dot, pos = 0, 0
        while i<n:
            if s[i] in ['+', '-']:
                i+=1
            if i>=n:
                return False
            if (ord(s[i])<ord('0') or ord(s[i])>ord('9')) and s[i]!='.':
                return False
            while i<n:
                if s[i] in ['e', 'E']:
                    break
                if s[i]=='.':
                    if dot == 1:
                        return False
                    else:
                        dot = 1
                    i+=1
                    continue
                if ord(s[i])<ord('0') or ord(s[i])>ord('9'):
                    return False
                pos = 1
                i+=1
            if i>=n:
                if pos==1:
                    break
                else:
                    return False
            else:
                i+=1
            if dot==1 and pos==0:
                return False
            if i>=n:
                return False
            if s[i] in ['+', '-']:
                i+=1
            if i>=n:
                return False
            while i<n:
                if ord(s[i])<ord('0') or ord(s[i])>ord('9'):
                    return False
                i+=1
        return True