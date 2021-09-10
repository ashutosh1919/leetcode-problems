# Time complexity: O(n)
# Approach: Two pointer approach by comparing one pointer from start and another pointer from end.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        n = len(s)
        i, j = 0, n-1
        while i<=j:
            while i<=j and not s[i].isalnum():
                i+=1
            while i<=j and not s[j].isalnum():
                j-=1
            if i>j:
                break
            if s[i]!=s[j]:
                return False
            i, j = i+1, j-1
        return True