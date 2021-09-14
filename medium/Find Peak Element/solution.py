# Time complexity: O(logn)
# Approach: Array contains increasing-decreasing numbers. We need to find any of such mountain.

class Solution:
    def binary(self, nums, start, end):
        if start==end:
            return start
        mid = (start+end)//2
        if nums[mid]>nums[mid+1]:
            return self.binary(nums, start, mid)
        return self.binary(nums, mid+1, end)
        
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        return self.binary(nums, 0, len(nums)-1)