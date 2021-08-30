# Time complexity: O(log(n))
# Approach: Binary search twice left and right

class Solution:
    def binaryLeft(self, nums, start, end, target, left):
        if start <= end:
            mid = (start+end)//2
            if nums[mid]==target:
                left = mid
                return self.binaryLeft(nums, start, mid-1, target, left)
            elif nums[mid]>target:
                return self.binaryLeft(nums, start, mid-1, target, left)
            else:
                return self.binaryLeft(nums, mid+1, end, target, left)
        return left
    
    def binaryRight(self, nums, start, end, target, right):
        if start <= end:
            mid = (start+end)//2
            if nums[mid]==target:
                right = mid
                return self.binaryRight(nums, mid+1, end, target, right)
            elif nums[mid]>target:
                return self.binaryRight(nums, start, mid-1, target, right)
            else:
                return self.binaryRight(nums, mid+1, end, target, right)
        return right
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binaryLeft(nums, 0, len(nums)-1, target, -1)
        right = self.binaryRight(nums, 0, len(nums)-1, target, -1)
        return [left, right]