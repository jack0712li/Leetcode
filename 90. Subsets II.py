class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        if len(nums) ==0:
            return []
        result =[]
        self.backtracking(nums,0,[],result)
        return result


    def backtracking(self, nums,startindex,path,result):


        
        result.append(path[:])

        for i in range(startindex,len(nums)):
            if i > startindex and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            self.backtracking(nums,i+1,path,result)
            path.pop()