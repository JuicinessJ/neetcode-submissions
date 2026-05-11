class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        curr_max = 0

        while left < right:

            max_area = min(heights[left], heights[right]) * (right - left)

            if curr_max < max_area:
                curr_max = max_area
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            
        return curr_max

        

# I am given list of numbers, representing heights of bars, and need to find the maximum volume of water by area.
# This volume or area is measured by the min of both bars * distance between both bars.
# For example: if we were given this list: [1,7,2,5,4,7,3,6], the best bars would be 7[1], and 6[7].
# This would calculate to min(7, 6) * (7 - 1) = 36

# I would want to use the two pointer approach, since we are recommended to stay within O(n) for time, and O(1).
# We will use the traditonal while left < right, and will not create any storage, as it isn't needed.
# Thought I may create a current_max and update this if a new max is found.
# Since this list provided is UO, I need to figure out how we'd increment or decrement left and right.
# I could compare them with the current_max, but how would this determine which we increment or decrement

# Figure Out:
# 
