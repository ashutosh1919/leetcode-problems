# Time complexity: O(2^(len(candidates)))
# Approach: Backtracking approach where the element can (1) either be there only this time (2) either be there this time and next times as well (3) not be there

class Solution:
    def recur(self, nums, i, target, tmp, ans):
        if i >= len(nums) or target==0:
            if target==0:
                if sorted(tmp) not in ans:
                    ans.append(sorted(tmp))
            return 
        if nums[i]>target:
            self.recur(nums, i+1, target, tmp, ans)
            return
        self.recur(nums, i+1, target, tmp, ans)
        self.recur(nums, i+1, target-nums[i], tmp+[nums[i]], ans)
        if target >= nums[i]:
            self.recur(nums, i, target-nums[i], tmp+[nums[i]], ans)
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []
        self.recur(candidates, 0, target, [], ans)
        return ans