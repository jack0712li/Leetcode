class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        cur = 0
        for i in range(0,len(nums)):
            cur = cur + nums[i]

            result = max(result,cur)

            if cur<0 :
                cur = 0

        return result
