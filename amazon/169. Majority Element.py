class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}

        max_num = 0
        result = nums[0]

        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1

            if seen[i] >= max_num:
                max_num = seen[i]
                result = i

        return result
        