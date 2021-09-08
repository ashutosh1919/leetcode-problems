# Time complexity: O(n*2^n)
# Approach: For each subset, iterate from 0 to n-1 and for each number in binary, take elements corresponding to 1s.

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        ans = []
        for i in range(2**n):
            tmp = []
            for j in range(n):
                if i & (1<<j):
                    tmp.append(nums[j])
            if tmp not in ans:
                ans.append(tmp)
        return ans