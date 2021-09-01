# Time complexity: O(2^(len(n)))
# Approach: Backtracking.

class Solution:
    def backTrack(self, nums, i, target, tmp, ans):
        if i>=len(nums) or target==0:
            if target==0:
                if sorted(tmp) not in ans:
                    ans.append(sorted(tmp))
            return
        for j in range(i, len(nums)):
            if j>i and nums[j]==nums[j-1]:
                continue
            if nums[j]>target:
                break
            self.backTrack(nums, j+1, target-nums[j], tmp+[nums[j]], ans)
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.backTrack(sorted(candidates), 0, target, [], ans)
        return ans