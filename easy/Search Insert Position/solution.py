# Time complexity: O(log(n))
# Approach: Binary search to calculate left bound.

class Solution:
    def binarySearch(self, nums, start, end, target, index):
        if start<=end:
            mid = (start+end)//2
            if nums[mid]==target:
                return self.binarySearch(nums, start, mid-1, target, mid)
            elif nums[mid]>target:
                return self.binarySearch(nums, start, mid-1, target, mid)
            else:
                return self.binarySearch(nums, mid+1, end, target, index)
        return index
        
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = self.binarySearch(nums, 0, len(nums)-1, target, -1)
        if target<=nums[0]:
            index = 0
        elif nums[len(nums)-1]<target:
            index= len(nums)
        return index