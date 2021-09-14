# Time complexity: O(n)
# Approach: Piegonhole sorting principle (https://www.geeksforgeeks.org/maximum-adjacent-difference-array-sorted-form/)

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return 0
        mx, mn = [-1]*(n-1), [sys.maxsize]*(n-1)
        mxv, mnv = max(nums), min(nums)
        delta = int(math.ceil((mxv-mnv)/(n-1)))
        for i in range(n):
            if nums[i]==mxv or nums[i]==mnv:
                continue
            index = (nums[i]-mnv)//delta
            if mx[index]==-1:
                mx[index] = nums[i]
            else:
                mx[index] = max(mx[index], nums[i])
            if mn[index]==sys.maxsize:
                mn[index] = nums[i]
            else:
                mn[index] = min(mn[index], nums[i])
        prev, mxgap = mnv, 0
        for i in range(n-1):
            if mn[i]==sys.maxsize:
                continue
            mxgap = max(mxgap, mn[i]-prev)
            prev = mx[i]
        mxgap = max(mxgap, mxv-prev)
        return mxgap