# Time complexity: O(len(nums))
# Approach: Two pointer solution

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n in [0, 1]:
            return n
        i, j, ans = 0, 1, 0
        while i<n and j<n:
            while j<n and nums[i]==nums[j]:
                j+=1
            if j< n:
                nums[i+1] = nums[j]
            ans+=1
            i+=1
        print(ans)
        return ans