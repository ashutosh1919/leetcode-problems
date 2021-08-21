# Time complexity: O(log(min(m,n)))
# Approach: Partitioning the combined array and finding mid point using binary search. You can find complete solution in this video https://youtu.be/LPFhl65R7ww

class Solution:
    def __init__(self):
        self.minInt = -10**6 - 1
        self.maxInt = 10**6 + 1
    
    def findMedian(self, nums):
        n = len(nums)
        if n == 0:
            return 0.
        if n % 2 == 0:
            return (nums[n//2] + nums[n//2]-1)/2.
        else:
            return nums[n//2]
    
    def partitionArrays(self, nums1, nums2, start, end):
        if start <= end:
            m = len(nums1)
            n = len(nums2)
            partX = (start+end)//2
            partY = (len(nums1)+len(nums2)+1)//2 - partX
            maxLeftX = self.minInt if partX == 0 else nums1[partX - 1]
            minRightX = self.maxInt if partX == m else nums1[partX]
            maxLeftY = self.minInt if partY == 0 else nums2[partY - 1]
            minRightY = self.maxInt if partY == n else nums2[partY]
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (m+n) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY))/2.
                else:
                    return float(max(maxLeftX, maxLeftY))
            elif maxLeftX > minRightY:
                return self.partitionArrays(nums1, nums2, start, partX-1)
            else:
                return self.partitionArrays(nums1, nums2, partX+1, end)
        return -1.
            
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        m, n = len(nums1), len(nums2)
        if m == 0:
            return self.findMedian(nums2)
        
                
        return self.partitionArrays(nums1, nums2, 0, m)
