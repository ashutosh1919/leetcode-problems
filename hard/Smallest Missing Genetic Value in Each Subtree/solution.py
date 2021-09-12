# Time complexity: O(n)
# Approach: We need to only find miss values from root to the index which has value 1. All other child nodes will have miss value 1.

class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        n = len(nums)
        res, children, seen = [1]*n, [[] for i in range(n)], [0]*100010
        if 1 not in nums:
            return res
        for i in range(1, n):
            children[parents[i]].append(i)
        
        def dfs(i):
            if seen[nums[i]]==0:
                for j in children[i]:
                    dfs(j)
                seen[nums[i]] = 1
        
        i, miss = nums.index(1), 1
        while i>=0:
            dfs(i)
            while seen[miss]:
                miss+=1
            res[i] = miss
            i = parents[i]
        return res