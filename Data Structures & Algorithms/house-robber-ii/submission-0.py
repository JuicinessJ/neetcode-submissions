class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp_first = [0] * (len(nums) + 1)
        dp_first[0] = nums[0]
        dp_first[1] = max(nums[0], nums[1])

        for i in range(2, len(nums) - 1):
            dp_first[i] = max(nums[i] + dp_first[i - 2], dp_first[i - 1])


        dp_second = [0] * (len(nums) + 1)
        dp_second[0] = 0
        dp_second[1] = nums[1]

        for i in range(2, len(nums)):
            dp_second[i] = max(nums[i] + dp_second[i - 2], dp_second[i - 1])

        return max(dp_first[len(nums) - 2], dp_second[len(nums) - 1])

        
        

"""
I am given a list of houses we can steal from, however, there are conditions.
I cannot steal from two adjacent houses, and cannot steal from the first AND last house, as this neighborhood is a circle
I am then asked to find the maxiumum amount of money we can steal from the houses given using the conditions provided above.

Based on the conditions, if we select the first house, we cannot select the last house, and vice versa.

If we proceed using a 1DP approach of tabulations, we first need to figure out our recurrence relation.

We know that if we select the first house, we cannot select the second house nor last house.
We should only select the first house if its value is greater than the second house and last house.

We also know that if we select the last house, we cannot select the first house nor the second to last.
We should only selec the last house if its value is greater than the first house and second to last.

We could attempt to compare the totals of robbing the first house to the second to last, and the second house to the last house, as these two approaches will meet the conditions.
"""