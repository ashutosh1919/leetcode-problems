# Time complexity: O(n)
# Approach: Solved using stack. Element is pushed in stack only if smaller than top element is iterated. This is done to find immidiately smaller left and right element of a particular element.

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st, max_area, n, i = [], 0, len(heights), 0
        while i<n:
            if not len(st) or heights[st[-1]]<=heights[i]:
                st.append(i)
                i+=1
            else:
                tp = st.pop()
                area = 0
                if len(st):
                    area = heights[tp]*(i-st[-1]-1)
                else:
                    area = heights[tp]*i
                max_area = max(max_area, area)
        while len(st):
            tp = st.pop()
            if len(st):
                area = heights[tp]*(i-st[-1]-1)
            else:
                area = heights[tp]*i
            max_area = max(max_area, area)
        return max_area
        