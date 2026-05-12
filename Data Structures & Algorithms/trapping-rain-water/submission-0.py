class Solution:
    def trap(self, height: List[int]) -> int:


# I am given a list of numbers, representing height or elevation within a map.
# I need to return the max possible volume of water that can be trapped within this map.

# I will be pursuing a two pointer approach, where I will use a while left < right
# However, with a twist, instead of right starting at the end, we'll have right always be left + 1.
# Because, our goal is to find possible "puddles", so the idea is we'll have the left stand at one location and the right extending until its larger than the left.
# Meaning the water would overflow out.
# Once we've solidified a puddle, we'll replace left with right value and increase right += 1.
# We'll keep incrementing both, until we find where left > right, meaning we have a possible puddle.
# This should keep running until we've reach the end.
# So maybe instead of while left < right, we'll have left < len()

# New Thought
# I want to continue using the two pointer approach, where I will use the while left < right.
# Where left starts at 0, and right at len() - 1, and I will want to have them converge.
# Instead of using a sliding window approach as the idea is above.
# I will compare the indexes values of their neighboring values and find their differences in height.
# By using a max() approach, and total that into a overall max. However, since we'll be running two pointers.
# It may be wise, to have a left max and right max, then at the end, total that and return the overall total.

        left, right = 0, len(height) - 1

        left_max, right_max = height[left], height[right]
        
        total = 0

        while left < right:

            if left_max < right_max:

                left += 1

                left_max = max(left_max, height[left])

                total += left_max - height[left]

            else:

                right -= 1

                right_max = max(right_max, height[right])

                total += right_max - height[right]

        return total

            
