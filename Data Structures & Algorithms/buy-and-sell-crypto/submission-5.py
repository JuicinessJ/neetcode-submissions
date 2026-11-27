class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        max_profit = 0

        while left <= right and right < len(prices):
            curr_profit = prices[right] - prices[left]

            if max_profit < curr_profit:
                max_profit = curr_profit

            if curr_profit < 0:
                left += 1

            else:
                right += 1

        return max_profit

        

# Input: list of numbers where each index represent the price of a stock
# Output: the maximum amount of money we could profit from buying low and selling high

# Since we are asked to find two points, a buy and sell, we can assume this is a two pointer problem. 
# The brute force approach would have us utilize two loops.
# One responsible for buying, other for selling, and tracking the running max_profit.
# However, to simplify this, we could utilize one loop.

# We would have two pointers, a left and right. Where the right is always ahead of left.
# Our left would be our buy, and right would be our sell.
# Our condition for advancing any pointer would be if our current_profit is positive or negative.
# All while keeping a running max_profit.
# Our left pointer would advance if the current profit is negative.