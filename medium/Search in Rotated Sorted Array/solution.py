# Time complexity: O(log(n))
# Approach: Modified binary search considering the pivot in every case.

class Solution:
    def isInInterval(self, a, b, target):
        print(a, b, target)
        if (a>b and b>=target) or (a==target) or (b==target):
            return True
        elif a>b and b<target:
            if a<=target:
                return True
            else:
                return False
        return a<=target and target<=b

    def binarySearch(self, nums, start, end, target):
        if start <= end:
            mid = (start+end)//2
            print(start, mid, end)
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                if self.isInInterval(nums[start], nums[mid], target):
                    return self.binarySearch(nums, start, mid-1, target)
                else:
                    return self.binarySearch(nums, mid+1, end, target)
            else:
                if self.isInInterval(nums[mid], nums[end], target):
                    return self.binarySearch(nums, mid+1, end, target)
                else:
                    return self.binarySearch(nums, start, mid-1, target)
        return -1
        
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1:
            return 0 if nums[0]==target else -1
        return self.binarySearch(nums, 0, len(nums)-1, target)