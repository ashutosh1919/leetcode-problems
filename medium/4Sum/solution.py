# Time complexity: O(n^3)
# Approach: Similar as 3 sum but it also has one more loop.

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = set()
        if n < 4:
            return ans
        nums = sorted(nums)
        for k in range(n):
            for l in range(k+1, n):
                s1 = target - (nums[k] + nums[l])
                i, j = l+1, n-1
                while i<j:
                    s2 = nums[i] + nums[j]
                    if s2 < s1:
                        i += 1
                    elif s2 > s1:
                        j -= 1
                    else:
                        ans.add((nums[k], nums[l], nums[i], nums[j]))
                        i += 1
                        j -= 1
        return ans