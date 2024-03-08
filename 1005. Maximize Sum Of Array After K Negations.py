class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort(key= lambda x:abs(x),reverse = True)

        for i in range(len(nums)):
            if nums[i] < 0 and k >0:
                nums[i] = -nums[i]
                k -= 1
            
        if k%2 == 1:
            nums[-1] = -nums[-1]

        return sum(nums)
            
        