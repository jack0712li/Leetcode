class Solution:

    def __init__(self):
        self.result = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        if len(candidates) == 0:
            return []

        self.backtracking(candidates,target,[],0,0)

        return self.result
        
        

    def backtracking(self,candidates,target,path,sum,index):

        if sum > target:
            return
        if sum == target:
            self.result.append(path[:])


        for i in range(index, len(candidates)):
            sum += candidates[i]
            path.append(candidates[i])
            self.backtracking(candidates,target,path,sum,i)
            sum -= candidates[i]
            path.pop()

