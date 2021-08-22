# Time complexity: O(n^2)
# Approach: Fix one and then based on that loop over other numbers.

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        minT, minD = 10**4+1, 10**4+1
        nums = sorted(nums)
        for k in range(n):
            rem = target - nums[k]
            i, j  = k+1, n-1
            while i<j:
                s = nums[i]+nums[j]
                diff = abs(target - (nums[i]+nums[j]+nums[k]))
                if diff <= minD:
                    minD = diff
                    minT = nums[i]+nums[j]+nums[k]
                if s < rem:
                    i += 1
                elif s > rem:
                    j -= 1
                else:
                    return target
        return minT