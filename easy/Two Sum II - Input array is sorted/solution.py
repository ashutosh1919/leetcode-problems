# Time complexity: O(n)
# Approach: Straight forward

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        i, j = 0, n-1
        while i<j:
            if nums[i]+nums[j]==target:
                return [i+1, j+1]
            elif nums[i]+nums[j]>target:
                j-=1
            else:
                i+=1
        return [-1, -1]