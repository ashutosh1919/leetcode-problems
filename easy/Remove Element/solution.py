# Time complexity: O(len(nums))
# Approach: Two pointer solution

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        if n == 0:
            return n
        if n == 1:
            return 0 if nums[0]==val else 1
        i, j, ans = 0, 1, 0
        while i<n:
            if nums[i]!=val:
                i+=1
                j+=1
                continue
            while j<n and nums[j]==val:
                j+=1
            if j<n:
                nums[i] = nums[j]
                nums[j] = val
            i+=1
            j+=1
        return len(nums) if val not in nums else nums.index(val)