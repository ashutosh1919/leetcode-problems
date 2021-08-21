# Time complexity: O(n)
# Approach: Manacher's Algorithm. Please watch this vide for explanation https://youtu.be/V-sEwsca1ak

class Solution:
    def longestPalindrome(self, s: str) -> str:
        newS = ""
        n = 2 * len(s) + 1
        ind = 0
        for j in range(n):
            if j % 2 == 1:
                newS += s[ind]
                ind += 1
            else:
                newS += "$"
        LPS = [0] * n
        start, end, i = 0, 0, 0
        while i < n:
            while start > 0 and end < n-1 and newS[start-1] == newS[end+1]:
                start -= 1
                end += 1
            LPS[i] = end - start + 1
            if end == n - 1:
                break
            newCenter = end + (1 if i%2==0 else 0)
            for j in range(i+1, end+1):
                LPS[j] = min(LPS[i-(j-i)], 2*(end-j)+1)
                if j + LPS[i-(j-i)]//2 == end:
                    newCenter = j
                    break
            i = newCenter
            start = i - LPS[i]//2
            end = i + LPS[i]//2
        ind, mx = 0, 0
        for j in range(n):
            if mx < LPS[j]:
                ind, mx = j, LPS[j]
        ans = ""
        start = ind - LPS[ind]//2
        end = ind + LPS[ind]//2
        for j in range(start, end+1):
            if newS[j] != "$":
                ans += newS[j]
        return ans
        