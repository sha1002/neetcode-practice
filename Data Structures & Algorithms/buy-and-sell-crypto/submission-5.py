class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        maximum_profit = 0

        for price in prices:
            lowest = min(lowest, price)
            maximum_profit = max(maximum_profit, price - lowest)

        return maximum_profit