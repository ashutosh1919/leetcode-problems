# Time complexity: O(n)
# Approach: Split the stripped string, reverse and join back as string.

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([x for x in s.strip().split() if x!=''][::-1])