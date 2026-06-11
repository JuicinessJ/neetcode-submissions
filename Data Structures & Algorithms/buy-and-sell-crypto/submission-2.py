class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_max = 0
        buy = prices[0]

        for i in range(1, len(prices)):

            sell = prices[i]

            curr_profit = sell - buy

            if curr_profit > curr_max:
                curr_max = curr_profit

            if buy > sell:
                buy = sell

        return curr_max