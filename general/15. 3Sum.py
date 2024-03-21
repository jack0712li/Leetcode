class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # 首先排序，目的是用双指针
        nums.sort()

        result = []

        for i in range(len(nums)):

            if nums[i] > 0:
                return result
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) -1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum == 0:
                    
                    result.append([nums[i],nums[left],nums[right]])
                    
                    # 由于题目要求不可以有重复的组合，所以这里要检查去重
                    while left < right and nums[left] == nums[left + 1]:
                        left+=1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1

                elif sum >0:
                    right -= 1
                else:
                    left += 1

        return result
