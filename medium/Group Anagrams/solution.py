# Time complexity: O(nlog(n)) where n is length of string in strs
# Approach: Sort all strings and group them

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        mp = {}
        tmp = strs.copy()
        for i in range(n):
            tmp[i] = ''.join(sorted(tmp[i]))
        for i in range(n):
            if tmp[i] in mp:
                mp[tmp[i]].append(strs[i])
            else:
                mp[tmp[i]] = [strs[i]]
        ans = []
        for k, v in mp.items():
            ans.append(v)
        return ans