class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        used = [False] * len(nums)

        self.backtracking(nums,used,[],result)

        return result


    def backtracking (self,nums,used,path,result):

        if len(nums) == len(path):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            path.append(nums[i])
            used[i] = True
            self.backtracking(nums,used,path,result)
            path.pop()
            used[i] = False