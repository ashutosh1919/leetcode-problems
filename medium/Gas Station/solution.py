# Time complexity: O(n)
# Approach: Straight forward solution (https://leetcode.com/problems/gas-station/discuss/1454600/Ideas-explained)

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n, tg, tc = len(gas), 0, 0
        for i in range(n):
            tg, tc = tg+gas[i], tc+cost[i]
        if tg<tc:
            return -1
        start, cur = 0, 0
        for i in range(n):
            cur+=(gas[i]-cost[i])
            if cur<0:
                cur, start = 0, i+1
        return start