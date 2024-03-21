class MyStack:
    
    # 偷懒了，用了deque自带的pop可以直接pop最右侧，实际上如果要用两个queue的，第二个queue作为存储存储第一个queue里面所有的数据除了最后一个进来的pop出去

    def __init__(self):

        self.queue = deque()
        

    def push(self, x: int) -> None:

        self.queue.append(x)
        

    def pop(self) -> int:

        if self.empty():
            return None

        return self.queue.pop()


        

    def top(self) -> int:
        if self.empty():
            return None

        result = self.queue.pop()

        self.queue.append(result)

        return result


        

    def empty(self) -> bool:

        return not self.queue
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()