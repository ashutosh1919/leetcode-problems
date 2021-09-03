# Time complexity: O(n)
# Approach: Accumulating the maximum reach.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        reach = -1
        for i in range(n):
            reach = max(reach, i+nums[i])
            if i==reach:
                break
        return reach>=n-1