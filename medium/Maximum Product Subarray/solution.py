# Time complexity: O(n)
# Approach: Modified Kadane's Algorithm

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx, mn, fl, ans = 1, 1, 0, 0
        for i in range(len(nums)):
            if nums[i]>0:
                mx = mx*nums[i]
                mn = min(mn*nums[i], 1)
                fl = 1
            elif nums[i]==0:
                mx, mn = 1, 1
            else:
                if mn*nums[i]>=1:
                    fl = 1
                mx, mn = max(mn*nums[i], 1), mx*nums[i]
            if ans<mx and fl==1:
                ans = mx
        if ans == 0:
            if 0 in nums:
                return 0
            return min(nums)
        return ans