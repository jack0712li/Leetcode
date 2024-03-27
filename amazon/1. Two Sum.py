class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            left = target - nums[i]
            if left in seen:
                return [seen[left],i]
            else:
                seen[nums[i]] = i

        return [0]
    
