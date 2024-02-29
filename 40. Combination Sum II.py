class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        candidates.sort()
        self.backtracking(candidates,target,0,[],0,result)

        return result

    def backtracking(self,candidates,target,sum,path,startindex,result):

        if sum == target:
            result.append(path[:])
            return

        for i in range(startindex,len(candidates)):
            if i > startindex and candidates[i] == candidates[i-1]:
                continue

            if sum > target:
                break

            sum += candidates[i]
            path.append(candidates[i])

            self.backtracking(candidates,target,sum,path,i+1,result)
            
            sum -= candidates[i]
            path.pop()
        