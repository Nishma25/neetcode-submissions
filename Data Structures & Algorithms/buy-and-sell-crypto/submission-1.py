class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minbuyP = prices[0]

        for sell in prices:
            maxP = max(maxP,sell- minbuyP)
            minbuyP = min(minbuyP,sell)

        return maxP        