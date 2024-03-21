class MyQueue:
    def __init__(self):

        self.myQueue = deque()

    def pop(self,value):
        if self.myQueue and self.myQueue[0] == value:
            self.myQueue.popleft()

    def push(self, value):
        while self.myQueue and self.myQueue[-1] < value:
            self.myQueue.pop()
        
        self.myQueue.append(value)

    def front(self):
        return self.myQueue[0]




class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        new_Queue = MyQueue()

        result = []

        for i in range(k):
            new_Queue.push(nums[i])

        result.append(new_Queue.front())
        for each in range(k,len(nums)):
            new_Queue.pop(nums[each-k])
            new_Queue.push(nums[each])
            top = new_Queue.front()
            result.append(top)

        return result


