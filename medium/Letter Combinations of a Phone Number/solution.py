# Time complexity: O(n^2)
# Approach: Use recursion in order to generate all possible combinations. Recursion makes it easy to implement. But same thing can be implemented using 2 for loops.

class Solution:
    def getCombinations(self, digits, i, st, strs, mp):
        if i >= len(digits):
            return strs
        
        for letter in mp[digits[i]]:
            if i == len(digits) - 1:
                strs.append(st+letter)
                continue
            self.getCombinations(digits, i+1, st+letter, strs, mp)
        return strs
    
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return ""
        mp = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        strs = []
        strs = self.getCombinations(digits, 0, "", strs, mp)
        return set(strs)