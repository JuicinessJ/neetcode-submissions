class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [0] * (len(nums) + 1)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[len(nums) - 1]
            

"""
I am asked to return the maximum amount of money we can steal from the given list, where each index represents a house.
However, we cannot steal from two houses that are adjacent, meaning if I chose n, where n represents a random number within the index, I cannot chose n - 1 or n - 2, as they'd be adjacent to n.

Since I am asked to find the maxiumm index at 0, could be part of the solution, but isn't guaranteed and houses at every other index may also not be considered optimal either.
As we may have an optimal solution at index at 0 and 3, since every other, would have us at 2.
This means, I will need to try n! combinations to find an optimal solution.
We're also not limited to the number of houses we can steal from, meaning our own condition is houses that aren't neighbors.



"""