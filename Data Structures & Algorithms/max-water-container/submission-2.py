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