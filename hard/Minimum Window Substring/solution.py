# Time complexity: O(ls*lt)
# Approach: Take frequency list for both the strings and keep checking for the same frequency whenever the number of chars matches.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ls, lt = len(s), len(t)
        if ls<lt:
            return ""
        fs, ft = [0]*256,  [0]*256
        start, start_index, min_length, ct = 0, -1, 10**5+1, 0
        for i in range(lt):
            ft[ord(t[i])] += 1
        for i in range(ls):
            fs[ord(s[i])] += 1
            if fs[ord(s[i])]<=ft[ord(s[i])]:
                ct += 1
            if ct == lt:
                while fs[ord(s[start])]>ft[ord(s[start])] or fs[ord(s[start])]==0:
                    if fs[ord(s[start])]>ft[ord(s[start])]:
                        fs[ord(s[start])] -= 1
                    start += 1
                lw = i-start+1
                if min_length > lw:
                    min_length = lw
                    start_index = start
        if start_index==-1:
            return ""
        return s[start_index:start_index+min_length]