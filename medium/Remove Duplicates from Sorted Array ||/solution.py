# Time complexity: O(n)
# Approach: 3 pointer solution. i is for changing values, j is for checking equality and track is for tracking the start of j.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return n
        i, j, track = 0, 0, 0
        while i<n and j<n:
            # print(nums, end=" ")
            j = track
            while j+1<n and nums[j]==nums[j+1]:
                j+=1
            if j-track>=1:
                nums[i] = nums[j]
                nums[i+1] = nums[j]
                i+=2
                j+=1
            else:
                nums[i] = nums[j]
                i+=1
                j+=1
            track = j
            # print(nums, i, j)
            if j>=n:
                break
        return i
                        