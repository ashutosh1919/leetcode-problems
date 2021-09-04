# Time complexity: O(log(x))
# Approach: Binary Search

class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        low, high = 1, x//2+1
        while low<high:
            mid = (low+high)//2
            sq = mid*mid
            if sq==x:
                return mid
            elif sq>x:
                high = mid
            else:
                low = mid+1
        return low-1