# Time complexity: O(len(s))
# Approach: We are pushing the character in the stack if it is opening bracket and whenever we iterate through closing bracket the top element of stack should be its corresponding opening bracket.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in ['(', '{', '[']:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if s[i] == ')' and top != '(':
                    return False
                if s[i] == '}' and top != '{':
                    return False
                if s[i] == ']' and top != '[':
                    return False
        return len(stack) == 0