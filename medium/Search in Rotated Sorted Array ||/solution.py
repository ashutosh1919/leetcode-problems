# Time complexity: O(log(n))
# Approach: Modified binary search.

class Solution:
    def binarySearch(self, nums, start, end, target):
        if start<=end:
            mid = (start+end)//2
            if nums[mid]==target:
                return True
            if nums[start]==nums[mid]:
                return self.binarySearch(nums, start+1, end, target)
            pA = nums[start]<=nums[mid]
            tA = nums[start]<=target
            if pA^tA:
                if pA:
                    return self.binarySearch(nums, mid+1, end, target)
                else:
                    return self.binarySearch(nums, start, mid-1, target)
            else:
                if nums[mid]<target:
                    return self.binarySearch(nums, mid+1, end, target)
                else:
                    return self.binarySearch(nums, start, mid-1, target)
        return False
    
    def search(self, nums: List[int], target: int) -> bool:
        return self.binarySearch(nums, 0, len(nums)-1, target)