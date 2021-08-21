# Time complexity: O(n)
# Approach: Window based mapping of characters and tracking of max length.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        mp = {}
        i, j, mx = 0, 0, 0
        while i < len(s) and j < len(s):
            mp[s[i]] = 1 if s[i] not in mp else mp[s[i]]+1
            if len(mp) == i-j+1:
                mx = max(mx, i-j+1)
            else:
                while len(mp) < i-j+1:
                    mp[s[j]] -= 1
                    if mp[s[j]] == 0:
                        del mp[s[j]]
                    j+=1
            i+=1
        return mx
                
                