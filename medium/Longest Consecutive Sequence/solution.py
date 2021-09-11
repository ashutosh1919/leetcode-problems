# Time complexity: O(n)
# Approach: Take streak and keep incrementing the number in set.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ls, nums = 0, set(nums)
        for num in nums:
            if num-1 not in nums:
                cn, cs = num, 1
                while cn+1 in nums:
                    cn, cs = cn+1, cs+1
                ls = max(ls, cs)
        return ls