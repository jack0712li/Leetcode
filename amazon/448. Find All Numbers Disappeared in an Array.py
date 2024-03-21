class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        seen = [0] *(len(nums)+1)
        result = []
        for i in nums:
            seen[i] += 1

        for j in range(1,len(seen)):
            if seen[j] == 0:
                result.append(j)

        return result
        