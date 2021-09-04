# Time complexity: O(n)
# Approach: Adding carry till it reaches the most significant digit and then if it still remains, then create new array and extend.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n, carry = len(digits), 0
        s = digits[n-1]+1
        digits[n-1], carry = s%10, s//10
        if not carry:
            return digits
        i = n-2
        while i>=0 and carry:
            s = digits[i]+carry
            digits[i], carry = s%10, s//10
            i-=1
        if carry:
            ans = []
            while carry:
                ans.append(carry%10)
                carry//=10
            ans = ans[::-1]
            ans.extend(digits)
            return ans
        return digits
        