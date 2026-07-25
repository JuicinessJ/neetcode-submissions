class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []
        total = 0

        def backtrack(i, total):
            # Total == Target
            if total == target:
                res.append(sol[:])
                return

            # Total is larger than Target
            if total > target or i >= len(nums):
                return

            # Don't Pick nums[i]
            backtrack(i+1, total)

            # Pick nums[i]
            sol.append(nums[i])
            backtrack(i, total + nums[i])
            sol.pop()

        backtrack(0, total)
        return res


"""
I am given a list of nums, and a target value, I am asked to find the set of combinations that equal our target value.
This means, for all the unique values within nums, I am asked to find in what combinations and quantity would equal our target value.
Since this is a backtracking problem, we are told our time complexity would be O(2^(t/m)) and O(t/m) for space...
where t is target and m is minimum value in the nums.

The methodology of a backtracking approach, is to create a tree where our final leaf nodes are the solution in a list.
To determine how to create this tree, we have two options, to choose or not choose that value.
While also recursing deeper with that value.

So for this problem, our base case is if the values we have selected for that node combined equal our target value.
However, there may be 3 possibility, where the set equal, less than, or greater than.
If the set equals our target value we stop, append into our solution, and return to stop the recursion for this combination of choices.
If the set is less than, we do nothing and allow it to continue recursing.
If the set is greater than, we stop the recursion and return nothing.




"""