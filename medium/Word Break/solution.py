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
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        root = TrieNode()
        for word in wordDict:
            root.addWord(word)

        @lru_cache(None)
        def dp(start):
            if start == n:  # Found a valid way to break words
                return True

            curr = root
            for end in range(start + 1, n + 1):  # O(N)
                c = s[end-1]
                if c not in curr.child: break
                curr = curr.child[c]
                if curr.isWord and dp(end):
                    return True
            return False

        return dp(0)
