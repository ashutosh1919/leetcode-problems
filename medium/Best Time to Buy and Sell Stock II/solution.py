# Time complexity: O(n)
# Approach: Relative positive difference of consecutive days

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = 0
        for i in range(1, len(prices)):
            if prices[i]>prices[i-1]:
                mx += prices[i]-prices[i-1]
        return mx