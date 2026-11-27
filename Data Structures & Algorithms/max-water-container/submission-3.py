class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_water = 0

        while left < right:
            amt_water = min(heights[left], heights[right]) * (right - left)

            if max_water < amt_water:
                max_water = amt_water

            if heights[left] > heights[right]:
                right -= 1

            elif heights[left] <= heights[right]:
                left += 1

        return max_water
        

# Input: list of numbers, each index representing the height of a line
# Output: maximum amount of water that can be stored between two indices.

# I know this is a two pointer problem, since we are looking to find the maximum amount of water stored between two points.
# To find the amount of water we are storing at any given time, I know the formula is the minimum of two heights * the distance between both points.
# Minimum since any water above the minimum will flow over.

# We'd first setup two pointers, on the opposite ends of our list.
# My greedy guess is that the pointer with the highest bar is what we keep, and we traverse the list with the lower bar. 