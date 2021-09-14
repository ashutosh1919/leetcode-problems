# Time complexity: O(logn)
# Approach: Binary Search

class Solution:
    def binarySearch(self, nums, start, end):
        if start<=end:
            # print(start, end)
            mid = (start+end)//2
            if mid==0 and nums[mid]<nums[mid+1]:
                return mid
            elif mid>0 and nums[mid]<nums[mid-1]:
                return mid
            elif mid<len(nums)-1 and nums[mid]>nums[mid+1]:
                return mid+1
            elif nums[end]<nums[start]:
                if nums[mid]>nums[start]:
                    return self.binarySearch(nums, mid+1, end)
                else:
                    return self.binarySearch(nums, start, mid-1)
            else:
                if nums[mid]>nums[start]:
                    return self.binarySearch(nums, start, mid-1)
                else:
                    return self.binarySearch(nums, mid+1, end)
        return -1
        
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        return nums[self.binarySearch(nums, 0, len(nums)-1)] 