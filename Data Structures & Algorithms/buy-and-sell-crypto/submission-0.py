class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_max = 0
        buy = prices[0]

        for i in range(1, len(prices)):

            sell = prices[i]

            curr_profit = sell - buy

            # print(buy, sell, curr_profit)

            if curr_profit > curr_max:
                curr_max = curr_profit

            if buy > sell:
                buy = sell

        return curr_max





# I am given a list of numbers, representing the prices of a stock of that particular ith day.
# I need to find the best time to buy and sell said stock. Buying at the lowest and selling at the highest.
# Returning the maximum profit I could expect from that list.

# To accomplish this, here are a few things I can immediately recognize.
# This will be using a sliding window solution, and I will need to keep track of the current highest profit at each iteration.
# Also, this is expected to be a O(n) for time, and O(1) for space complexity.
# Meaning no storage and one loop.

# Now, this curr_max should only be updated when curr_profit > curr_max.
# As for finding the best time to buy and sell, I could consider iterating through the full list, and finding the lowest and highest value.
# But the issue would be if the lowest is after the highest or highest is before.
# So I shouldn't try this, but could still attempt to adapt to that solution.
# Where I will only update the lowest if the value is before the highest.

# The other would be a two loop solution, where the outer loop declares the buy and the inner loop is sell.
# With the inner loop start buy + 1, this would work, but again, this is expected to be O(n).

# Since I am expected to make a O(n) solution, I could try updating the buy value with i + 1 if the i + 1 is less than.
# While the loop keeps checking what the buy and sell price would be and updating curr_max if the curr_profit is greather

# So the idea would be I create one loop. This loop will iterate from start to end.
# Inside, I will find out what the curr_profit would be by checking our current buying value compared to ith (selling).
# If curr_profit > curr_max, we update curr_max.
# If ith < buy, we update buy with ith, and continue iterating through the list