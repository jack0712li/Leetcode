class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        self.backTracking(nums,[],[False]*len(nums),result)
        return result


    def backTracking(self,nums,path,used,result):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1] and not used[i-1]:
                continue

            if used[i]:
                continue

            path.append(nums[i])
            used[i] = True
            self.backTracking(nums,path,used,result)
            used[i] = False
            path.pop()
        