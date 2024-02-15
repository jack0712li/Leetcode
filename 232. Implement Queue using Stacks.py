class MyQueue:


# 用list 来建造一个FIFO的队列。 python没有stack 但是和list的功能一样
    def __init__(self):
        self.stack_in = []
        self.stack_out = []
        

    def push(self, x: int) -> None:
        self.stack_in.append(x);
        

    def pop(self) -> int:

        if self.empty():
            return None

        self.dupmstackout()

        return self.stack_out.pop()

    def peek(self) -> int:

        if self.empty():
            return None

        self.dupmstackout()

        result = self.stack_out.pop()
        self.stack_out.append(result)
        return result

        

    def empty(self) -> bool:

        return (not self.stack_in and not self.stack_out)
        
    def dupmstackout(self):
        if len(self.stack_out) == 0:
            while len(self.stack_in) != 0:
                self.stack_out.append(self.stack_in.pop())
            

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()