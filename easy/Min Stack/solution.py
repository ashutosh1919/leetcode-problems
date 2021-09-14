# Time complexity: O(n)
# Approach: Implementation using 2 arrays.

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if len(self.minStack)==0:
            self.stack.append(val)
            self.minStack.append(val)
        else:
            if val > self.minStack[-1]:
                self.minStack.append(self.minStack[-1])
            else:
                self.minStack.append(val)
            self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()