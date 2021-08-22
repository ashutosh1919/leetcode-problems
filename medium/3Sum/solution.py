# Time complexity: O(n^2)
# Approach: Fix one and then based on that loop over other numbers.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        nums = sorted(nums)
        ans = []
        for k in range(n):
            target = -nums[k]
            i, j = k+1, n-1
            while i<j:
                s = nums[i] + nums[j]
                if s < target:
                    i += 1
                elif s > target:
                    j -= 1
                else:
                    ans.append((nums[k], nums[i], nums[j]))
                    i += 1
                    j -= 1
                    
        return set(ans)