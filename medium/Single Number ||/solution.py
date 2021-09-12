# Time complexity: O(n)
# Approach: Sum the bits of i and or the result for whichever bit mod of 3 is nonzero.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n, result = len(nums), 0
        for i in range(32):
            sm, x = 0, (1<<i)
            for j in range(n):
                if abs(nums[j])&x:
                    sm+=1
            if sm%3!=0:
                result |= x
        ct = 0
        for num in nums:
            if num==result:
                ct+=1
        return result if ct==1 else -result