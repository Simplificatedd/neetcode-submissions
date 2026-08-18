class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute force
        max_profit = 0
        for i, num in enumerate(prices):
            for i2, num2 in enumerate(prices):
                if i2 <= i:
                    continue
                difference = num2 - num
                if difference > max_profit and difference > 0:
                    max_profit = difference
        return max_profit