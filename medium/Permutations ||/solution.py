# Time complexity: O(len(nums)!)
# Approach: Same algorithm as Permutation with distinct numbers.

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        if n == 1:
            return [nums]
        ans = [nums.copy()]
        while True:
            i = n-2
            while i>=0 and nums[i]>=nums[i+1]:
                i-=1
            if i<0:
                break
            j = n-1
            while j>i and nums[j]<=nums[i]:
                j-=1
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            nums[i+1:] = nums[i+1:][::-1]
            ans.append(nums.copy())
        return ans