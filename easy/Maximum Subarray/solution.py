# Time complexity: O(n)
# Approach: Kadane's Algorithm

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        cur, mx = 0, 0
        for i in range(n):
            cur+=nums[i]
            mx = max(mx, cur)
            if cur<0:
                cur = 0
        if mx == 0:
            mx = max(nums)
        return mx