# Time complexity: O(n*2)
# Approach: Dynamic Programming Solution

class Solution:
    def minCut(self, s: str) -> int:
        dp=[[False]*len(s) for _ in range(len(s))]
        
        for g in range(len(s)):
            i=0
            for j in range(g,len(s)):
                if g==0:
                    dp[i][j]=True
                elif g==1:
                    dp[i][j]=(s[i]==s[j])
                else:
                    if s[i]==s[j] and dp[i+1][j-1]==True:
                        dp[i][j]=True
                    else:
                        dp[i][j]=False
                i+=1
                
#         here for storing min cut
        storage=[0]*len(s)
        storage[0]=0
        
        for j in range(1,len(storage)):
            if dp[0][j]==True:
                #if till that index all string is palindrome then min cut is 0
                storage[j]=0
            else:
                mn=sys.maxsize
                for i in range(1,j+1):#1 because when satrt with 0 then that acomplete string
                    if dp[i][j]==True and storage[i-1]<mn:
                        mn=min(mn,storage[i-1])

                storage[j]=mn+1

        return storage[-1]