# Time complexity: O(n*n)
# Approach: BFS to generate shortest depth solution.

class Solution:
    def findNbs(self, cur, word_list):
        nbs = set()
        for i in range(len(cur)):
            for char in 'qwertyuiopasdfghjklzxcvbnm':
                ns = cur[:i]+char+cur[i+1:]
                if ns in word_list:
                    nbs.add(ns)
        return nbs
    
    def bfs(self, bword, eword):
        word_list = self.word_list.copy()
        q, vis = deque(), set()
        q.append((bword, 1))
        while q:
            word_list -= set(q)
            sz = len(q)
            for i in range(sz):
                cur, pt = q.popleft()
                if cur==eword:
                    return pt
                nbs = self.findNbs(cur, word_list)
                for nb in nbs:
                    if nb not in vis:
                        q.append((nb, pt+1))
                        vis.add(nb)
        return 0
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        self.word_list = set(wordList)
        if endWord not in self.word_list:
            return 0
        return self.bfs(beginWord, endWord)