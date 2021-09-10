# Time complexity: O(n*n) where n is word_list
# Approach: BFS to find neighbors and recursion to find the paths.

class Solution:
    def findNbrs(self, cur, word_list):
        nbrs = set()
        for i in range(len(cur)):
            for char in 'qwertyuiopasdfghjklzxcvbnm':
                ns = cur[:i]+char+cur[i+1:]
                if ns in word_list:
                    nbrs.add(ns)
        return nbrs
    
    def bfs(self, bword):
        word_list = self.word_list.copy()
        que = deque()
        que.append(bword)
        while que:
            word_list -= set(que)
            sz = len(que)
            for i in range(sz):
                cur = que.popleft()
                nbs = self.findNbrs(cur, word_list)
                for nb in nbs:
                    self.adj_list[cur].add(nb)
                    que.append(nb)
    
    def backTrack(self, bword, eword, tmp, result):
        if bword==eword:
            result.append(tmp.copy())
        if bword not in self.adj_list:
            return
        for word in self.adj_list[bword]:
            self.backTrack(word, eword, tmp+[word], result)
    
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        self.word_list = set(wordList)
        self.adj_list = defaultdict(set)
        result = []
        if endWord not in wordList:
            return result
        self.bfs(beginWord)
        self.backTrack(beginWord, endWord, [beginWord], result)
        return result