class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) - 1

        while low <= high:

            mid = low + (high - low) // 2

            val = nums[int(mid)]

            if val < target:
                low = mid + 1

            elif val > target:
                high = mid - 1

            else:
                return mid

        return -1

# I am given a sorted list in ascending order, and a target value.
# This target value represents that value I am searching for, utilizing a binary search.
# I need to return the index where this value lies, within this sorted list.

# I am to use a binary search, as my constraits require me to stay within O(logn) for time, and O(1) for space.
# I will utilize a while loop, where I check if our declared low value is less than our declared high value.
# As we iterate through, we'll need to calculate our middle value, this will be used to split our list into halves
# If our middle value is less than target, we increase our low-end by mid + 1
# If our middle is greater than target, we decrease our high-end by mid - 1
# Else we return the mid