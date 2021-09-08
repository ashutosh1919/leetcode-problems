# Time complexity: O(n)
# Approach: Backtracking. Similar to DP 2D array solution.

class Solution:
    def findIp(self, s, index, i, tmp, ans):
        if i==4:
            if index >= len(s):
                ans.append(tmp[1:])
            return
        if index >= len(s):
            return
        if s[index]=='0':
            self.findIp(s, index+1, i+1, tmp+'.'+s[index], ans)
        else:
            if int(s[index])>=0 and int(s[index])<=255:
                self.findIp(s, index+1, i+1, tmp+'.'+s[index], ans)
            if index+2<=len(s) and int(s[index:index+2])>=0 and int(s[index:index+2])<=255:
                self.findIp(s, index+2, i+1, tmp+'.'+s[index:index+2], ans)
            if index+3<=len(s) and int(s[index:index+3])>=0 and int(s[index:index+3])<=255:
                self.findIp(s, index+3, i+1, tmp+'.'+s[index:index+3], ans)

    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        self.findIp(s, 0, 0, "", ans)
        return ans