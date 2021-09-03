# Time complexity: O(n)
# Approach: Strip + Split + Return length of last element

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])