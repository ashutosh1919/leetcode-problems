# Time complexity: O(n)
# Approach: Dynamic Programming (https://www.geeksforgeeks.org/minimum-number-of-jumps-to-reach-end-of-a-given-array/)

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            nums[i] = max(nums[i]+i, nums[i-1])
        j, ans = 0, 0
        while j<n-1:
            ans+=1
            j = nums[j]
        return ans