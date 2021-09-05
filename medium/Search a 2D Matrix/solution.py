# Time complexity: O(log(max(m, n)))
# Approach: Binary search 2 times. First over rows and then columns.

class Solution:
    def binarySearch(self, matrix, start, end, target, fixed=-1):
        if start<=end:
            mid = (start+end)//2
            if fixed == -1:
                if matrix[mid][0]<=target and matrix[mid][len(matrix[0])-1]>=target:
                    return mid
                elif matrix[mid][0]>target:
                    return self.binarySearch(matrix, start, mid-1, target)
                else:
                    return self.binarySearch(matrix, mid+1, end, target)
            else:
                if matrix[fixed][mid]==target:
                    return mid
                elif matrix[fixed][mid]>target:
                    return self.binarySearch(matrix, start, mid-1, target, fixed)
                else:
                    return self.binarySearch(matrix, mid+1, end, target, fixed)
        return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.binarySearch(matrix, 0, len(matrix)-1, target)
        if row==-1:
            return False
        col = self.binarySearch(matrix, 0, len(matrix[0])-1, target, row)
        return col!=-1