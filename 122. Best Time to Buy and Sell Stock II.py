class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = [0] * (len(prices) -1)
        result = 0
        for i in range(len(prices)-1):
            profit[i] = prices[i+1] - prices[i]

        for each in profit:
            if each > 0:
                result += each

        return result
            
        