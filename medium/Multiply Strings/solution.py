# Time complexity: O(n1*n2)
# Approach: Applying loops to both the numbers in the same way we do the manual computation of multiplication.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=='0' or num2=='0':
            return '0'
        num1, num2 = num1[::-1], num2[::-1]
        n1, n2 = len(num1), len(num2)
        ans = [0]*(n1+n2)
        for i in range(n1):
            for j in range(n2):
                ans[i+j] += int(num1[i]) * int(num2[j])
                ans[i+j+1] += ans[i+j]//10
                ans[i+j] %= 10
        size = len(ans)-1
        while size>=0 and ans[size]==0:
            size-=1
        ans = ''.join(map(str, ans[size::-1]))
        return ans
        
        
            
            