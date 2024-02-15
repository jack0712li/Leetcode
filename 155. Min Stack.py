class MinStack:

    # 很聪明的方法，我们只需要记录每次最低的输入就好，不需要记录所有输入

    def __init__(self):

        self.stack = []
        self.minstack = []
    def push(self, val: int) -> None:

        self.stack.append(val)

        min_val = min(val, self.minstack[-1] if self.minstack else val)

        self.minstack.append(min_val)

        

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()