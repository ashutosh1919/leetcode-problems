# Time complexity: O(n*n)
# Approach: Mathematical solution for directly finding kth sequence (https://www.youtube.com/watch?v=wT7gcXLYoao).

class Solution:
    def calcFact(self, n):
        fact = [1]
        prod = 1
        for i in range(1, n+1):
            prod *= i
            fact.append(prod)
        return fact
    
    def getPermutation(self, n: int, k: int) -> str:
        k-=1
        st = set()
        fact = self.calcFact(n)
        prev, res = [str(i) for i in range(1, n+1)], []
        while len(prev)>0:
            left = len(prev)-1
            # print(k, fact[left], prev)
            first_pos = k//fact[left]
            first_el = prev[first_pos]
            prev.remove(first_el)
            res.append(first_el)
            k = k%fact[left]
        return ''.join(res)
        