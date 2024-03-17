class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0
        
        maxProfit = 0
        minPrice = prices[0]

        for price in prices:
            minPrice = min(price,minPrice)
            profit = price - minPrice
            maxProfit = max(maxProfit , profit)
        
        return maxProfit



        