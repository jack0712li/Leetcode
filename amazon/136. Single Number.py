class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}

        for i in nums:
            if i not in seen:
                seen[i] = 0
            seen[i] += 1

        for key , val in seen.items():
            if val == 1:
                return key

        return -1