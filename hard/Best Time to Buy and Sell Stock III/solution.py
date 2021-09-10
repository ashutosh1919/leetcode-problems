# Time complexity: O(n)
# Approach: Making first transaction and making second transaction from the profit of first one.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n, fp, fs, sp, ss = len(prices), -10**5-1, 0, -10**5-1, 0
        for i in range(n):
            fp = max(fp, -prices[i])
            fs = max(fs, fp+prices[i])
            sp = max(sp, fs-prices[i])
            ss = max(ss, sp+prices[i])
        return ss