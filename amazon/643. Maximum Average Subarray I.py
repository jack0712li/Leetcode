class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        avg = 0
        sum = 0
        left = 0
        for i in range(k):
            sum += nums[i] 
        
        avg = sum / k
        for j in range(k,len(nums)):
            sum -= nums[left]
            left += 1
            sum += nums[j]
            avg = max(avg,sum/k)

        return avg