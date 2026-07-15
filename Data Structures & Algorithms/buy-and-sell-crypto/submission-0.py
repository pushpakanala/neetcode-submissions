class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price          # found a new cheapest buy day
            else:
                profit = price - min_price # profit if we sold today
                max_profit = max(max_profit, profit)
        
        return max_profit
