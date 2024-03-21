class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        size = len(nums) 
        sum = size*(size+1) /2
        cur_sum = 0
        for i in nums:
            cur_sum += i

        return int(sum - cur_sum)


        