# Time complexity: O(len(height))
# Approach: Take left and right boundry that will be the base area then move inwards in with end which has lower height.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        start, end, mx = 0, n-1, 0
        while start < end:
            area = min(height[start], height[end]) * (end - start)
            mx = max(mx, area)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return mx
        
            