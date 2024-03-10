#first
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # 用于记录查询过的数字
        record ={}
        
        for i in range(len(nums)):
            left = target - nums[i]
            # 查询是否已经被记录过，如果记录过则返回
            if left in record:
                return [record[left],i]
            
            else:
                record[nums[i]] = i
        return [0]
                            
        
        break
        
        
# @lc code=end

