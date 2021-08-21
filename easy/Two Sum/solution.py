# Time complexity: O(nlogn)
# Approach: iterate through the list keeping the track of available elements and their indices in dict. When the complementry item arrives, return the indices.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            b = target - nums[i]
            if b in mp:
                return [i, mp[b]]
            mp[nums[i]] = i
                
        return []