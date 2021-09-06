# Time complexity: O(2^n)
# Approach: Recursively extracting the permutations

class Solution:
    def permute(self, n, k, i, tmp, ans):
        if k==0:
            ans.append(tmp)
            return
        if i>n:
            return
        self.permute(n, k, i+1, tmp, ans)
        self.permute(n, k-1, i+1, tmp+[i], ans)
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        self.permute(n, k, 1, [], ans)
        return ans