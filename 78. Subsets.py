class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        result = []

        self.backtracking(nums,0,[],result)

        return result
 
    def backtracking(self,nums,startindex,path,result):

        result.append(path[:])


        for i in range(startindex,len(nums)):
            path.append(nums[i])
            self.backtracking(nums,i+1,path,result)
            path.pop()

        

        