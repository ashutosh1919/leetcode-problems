# Time complexity: O(n)
# Approach: Accumulate min value from left and max value from right for all indexes and get the maximum difference.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        minA, maxA = [10**4]*n, [0]*n
        minA[0], maxA[n-1] = prices[0], prices[n-1]
        if n==1:
            return 0
        for i in range(1, n):
            minA[i] = min(prices[i], minA[i-1])
        for i in range(n-2, -1, -1):
            maxA[i] = max(prices[i], maxA[i+1])
        ans = 0
        for i in range(n):
            ans = max(ans, abs(maxA[i]-minA[i]))
        return ans