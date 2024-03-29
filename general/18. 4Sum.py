class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # 这道题和three sum 一样知识需要多套一个for loop 把时间从 n^4 优化到 n^3

        nums.sort()
        result = []

        for i in range(len(nums)):

            if nums[i] > target and target > 0 and nums[i] > 0:
                break            
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] > target and target > 0:
                    break
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                left = j + 1
                right = len(nums) -1

                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if sum > target:
                        right -= 1
                    elif sum < target:
                        left += 1
                    else:
                        result.append([nums[i],nums[j],nums[left],nums[right]])
                        
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        
                        left += 1
                        right -= 1

        return result


        