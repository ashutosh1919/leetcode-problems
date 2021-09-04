# Time complexity: O(max(la, lb))
# Approach: Brute force solution.

class Solution:
    def bsum(self, a, b):
        return int(a)+int(b)
    
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        la, lb, i, j, carry = len(a), len(b), 0, 0, 0
        ans = []
        while i<la and j<lb:
            s = self.bsum(a[i], b[j]) + carry
            ans.append(str(s%2))
            carry, i, j = s//2, i+1, j+1
        while i<la:
            s = int(a[i])+carry
            ans.append(str(s%2))
            carry, i = s//2, i+1
        while j<lb:
            s = int(b[j])+carry
            ans.append(str(s%2))
            carry, j = s//2, j+1
        while carry:
            ans.append(str(carry%2))
            carry //= 2
        return ''.join(ans)[::-1]
            