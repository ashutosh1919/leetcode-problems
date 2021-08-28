# Time complexity: O(nlogn)
# Approach: Standard algorithm of NextPermute given in https://www.nayuki.io/page/next-lexicographical-permutation-algorithm

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n==0:
            return
        j = n-2
        while j>=0 and nums[j]>=nums[j+1]:
            j -= 1
        print(j)
        if j<0:
            nums.sort()
            return
        i = n-1
        while i>j:
            if nums[i]>nums[j]:
                break
            i -= 1
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
        nums[j+1:] = nums[j+1:][::-1] 
        return