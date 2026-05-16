class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        min_val = nums[0]

        while left <= right:

            mid = (left + right) // 2

            print(f"Mid: {nums[mid]}")

            if nums[mid] > nums[right]:
                left = mid + 1

            else:
                right = mid - 1

            # Checks incase our mid val happens to be min
            min_val = min(min_val, nums[mid])

        return min_val



        

# I am given a list of numbers, numbers that used to be sorted in an ascending order.
# However, this list has been rotated, where the tail numbers, have been pushed towards the head.
# I am asked to find the minimum number within this once sorted list, constraining myself within a O(logn) time, and O(1) for space.

# A brute force would have us, iterating through the list, with one loop, and keeping track the active min element.
# However, since we are tasked to use a binary search functionality, we cannot.
# Instead we need to take into consideration how we could update our low and high, or left and right, with a middle value in mind.
# Knowing that this list is no longer sorted, we cannot try sorting this, as this would take O(n^2).
# We could try something else, where to check if our middle value is greater or less than the first value index @ 0.
# If our middle value is less than, then we know our right half is the relevant section.
# However, this is already obvious since our list has been rotated.
# Instead we should consider finding the middle value, and check its neighbors.
# If the left neighbor is decreasing, then we know we need this section, as it'll lead to our smallest number.
# If our right section is decreasing then we know our middle value so happens to be formerly the right-most value.
# Morale of the story, we are looking for the pattern of decreasing.
# However, what if our middle value so happens to be our min value.
# We could create a catch, that actively updates our min_val with the middle value at each iteration.