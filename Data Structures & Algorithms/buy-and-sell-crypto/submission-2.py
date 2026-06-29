class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = prices[0]
        profit = 0
        for price in prices[1:]:
            minP = min(price, minP)
            profit = max(price-minP, profit)
        
        return profit