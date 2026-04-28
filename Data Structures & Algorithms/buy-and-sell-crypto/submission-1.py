class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = 10**9
        maxP = 0

        for price in prices:
            if price < minP:
                minP = price
            profit = price - minP

            if profit > maxP:
                maxP = profit
        
        return maxP