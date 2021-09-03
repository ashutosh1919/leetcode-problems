# Time complexity: O(n)
# Approach: Insert the new interval at certain position and then apply merge.

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i, n = 0, len(intervals)
        while i<n and newInterval[0]>=intervals[i][0]:
            i+=1
        intervals.insert(i, newInterval)
        i, n = 0, len(intervals)
        ans = []
        while i<n:
            start, end, j = intervals[i][0], intervals[i][1], i+1
            while j < n:
                if intervals[j][0]<=end:
                    end = max(intervals[j][1], end)
                    j+=1
                else:
                    break
            ans.append([start, end])
            i = j
        return ans
        