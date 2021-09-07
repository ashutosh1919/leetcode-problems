# Time complexity: O(n^2) where n is length of string
# Approach: Recursion with memoizing boolean values.

class Solution:
    def __init__(self):
        self.mp = {}
    
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1)!=len(s2):
            return False
        n = len(s1)
        if not n or s1==s2:
            return True
        if sorted(s1)!=sorted(s2):
            return False
        if s1+' '+s2 in self.mp:
            return self.mp[s1+' '+s2]
        fl = False
        for i in range(1, n):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                fl = True
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                fl = True
                return True
        self.mp[s1+' '+s2] = fl
        return self.mp[s1+' '+s2]