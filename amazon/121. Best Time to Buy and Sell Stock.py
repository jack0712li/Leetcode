    class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = 10001
        profit = 0
        for i in prices:
            if i < min_price:
                min_price = i

            profit = max(profit,i-min_price)
        if profit > 0:
            return profit

        else:
            return 0

            
        