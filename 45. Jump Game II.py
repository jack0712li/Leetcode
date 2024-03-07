class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        cur_dis = 0
        next_dis = 0
        steps = 0

        for i in range(len(nums) -1):
            next_dis = max(i + nums[i],next_dis)
            if i == cur_dis:
                steps += 1
                cur_dis = next_dis
                if next_dis >= len(nums):
                    break

        return steps
        