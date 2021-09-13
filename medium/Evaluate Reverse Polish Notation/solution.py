# Time complexity: O(n)
# Approach: Use stack to track parameters pop 2 params when operator is iterated.

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n, st = len(tokens), []
        if n==1:
            return int(tokens[0])
        for i in range(n):
            # print(st)
            if tokens[i] not in '+-/*':
                st.append(int(tokens[i]))
                continue
            b = st.pop()
            a = st.pop()
            if tokens[i]=='+':
                exp = (a+b)
            elif tokens[i]=='-':
                exp = (a-b)
            elif tokens[i]=='*':
                exp = (a*b)
            elif tokens[i]=='/':
                exp = int(a/b)
            st.append(exp)
        return exp