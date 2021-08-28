# Time complexity: O(len(s)*len(words)*len(words[0]))
# Approach: Window matching with the window length len(words)*word_length

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        mp = {}
        for st in words:
            mp[st] = 1 if st not in mp else mp[st]+1
        i, ans, wlen = 0, [], len(words[0])
        elen = wlen*len(words)
        while i+elen<=n:
            subst = s[i:i+elen]
            tmp = mp.copy()
            j = 0
            while j < len(subst):
                tst = subst[j:j+wlen]
                if tst in tmp:
                    tmp[tst] -= 1
                    if tmp[tst] == 0:
                        del tmp[tst]
                else:
                    break
                j = j + wlen
            if len(tmp)==0:
                ans.append(i)
            i = i+1
            if i==n:
                break
        return ans