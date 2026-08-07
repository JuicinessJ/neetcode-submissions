class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for n in nums:
            if n in seen:
                return True

            elif n not in seen:
                seen.add(n)

        return False


            



"""
We are given an array nums, each representing an integer, which may appear more than one.

We are asked to determine if any unique integer appears more than once.

We will use a hashset, where we add integers into this, and if another value appears again, we return True immediately, else False.

"""