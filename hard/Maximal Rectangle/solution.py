# Time complexity: O(m*n)
# Approach: Find largest rectangle in histogram (each row) and accumulate results of each row

class Solution:
    def maxHist(self, row):
        n, max_area, st, i = len(row), 0, [], 0
        while i<n:
            if not len(st) or row[st[-1]]<=row[i]:
                st.append(i)
                i+=1
            else:
                tp_val = row[st.pop()]
                area = tp_val * i
                if len(st):
                    area = tp_val * (i-st[-1]-1)
                max_area = max(max_area, area)
        while len(st):
            tp_val = row[st.pop()]
            area = tp_val * i
            if len(st):
                area = tp_val * (i-st[-1]-1)
            max_area = max(max_area, area)
        return max_area
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix)==0:
            return 0
        m, n = len(matrix), len(matrix[0])
        if m==0 or n==0:
            return 0
        for i in range(m):
            for j in range(n):
                matrix[i][j] = int(matrix[i][j])
        res = self.maxHist(matrix[0])
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j]:
                    matrix[i][j] += matrix[i-1][j]
            res = max(res, self.maxHist(matrix[i]))
        return res