# Time complexity: O(n)
# Approach: Segregate all positive numbers and then invert their indexes.

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Segregate positive numbers on right side of array
        size = 0
        for i in range(n):
            if nums[i]<=0:
                # Swap
                tmp = nums[i]
                nums[i] = nums[size]
                nums[size] = tmp
                size += 1
        
        # Invert all numbers' index which are present
        nums = nums[size:]
        n = len(nums)
        for i in range(n):
            if abs(nums[i])-1 < n and nums[abs(nums[i])-1]>0:
                nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]
        for i in range(n):
            if nums[i]>0:
                return i+1
        return n+1