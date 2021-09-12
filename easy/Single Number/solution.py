# Time complexity: O(n)
# Approach: XOR of two same number is 0.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(1, len(nums)):
            ans ^= nums[i]
        return ans