# Time complexity: O(log(n))
# Approach: Just divide power by 2 and keep multiplying the resultant.

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0. or x == 1.:
            return x
        if n in [-1, 0, 1]:
            return x**n
        tmp = self.myPow(x,(n-1)//2) if (n%2) else self.myPow(x,n//2)
        return tmp*tmp*x if (n%2) else tmp*tmp