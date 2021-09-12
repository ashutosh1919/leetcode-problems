# Time complexity: O(n*n)
# Approach: Storing words in Trie and applying dfs.

class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.isWord = False
    
    def addWord(self, word):
        curr = self
        for c in word:
            curr = curr.child[c]
        curr.isWord = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        root = TrieNode()
        for word in wordDict:
            root.addWord(word)
        
        def dfs(start, tmp, ans):
            nonlocal n
            nonlocal root
            nonlocal s
            if start == n:
                ans.append(tmp.strip())
                return
            
            curr = root
            for end in range(start+1, n+1):
                c = s[end-1]
                if c not in curr.child:
                    return
                curr = curr.child[c]
                if curr.isWord:
                    dfs(end, tmp+s[(start):end]+' ', ans)
        ans = []
        dfs(0, "", ans)
        return ans