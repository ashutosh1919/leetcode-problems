# Time complexity: O((2^n)*n)
# Approach: For each subset, iterate from 0 to n-1 and for each number in binary, take elements corresponding to 1s.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        for i in range(2**n):
            tmp = []
            for j in range(n):
                if i & (1<<j):
                    tmp.append(nums[j])
            ans.append(tmp)
        return ans