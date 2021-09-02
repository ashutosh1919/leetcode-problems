# Time complexity: O(n)
# Approach: Pre-computing arrays containing information about max height poles around it. With that, finding the water contained over specific position becomes easier.

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 1:
            return 0
        left, right = [0]*n, [0]*n
        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(height[i], left[i-1])
        right[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right[i] = max(height[i], right[i+1])
        ans = 0
        for i in range(n):
            ans += (min(left[i], right[i])-height[i])
        return ans
                