# Time complexity: O(n)
# Approach: Sort the intervals array, take first interval and keep expanding till it's valid. Repeat same for remaining.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
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
            