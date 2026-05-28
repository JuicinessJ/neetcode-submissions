class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            print(left, right, mid)    
            print(f"left = {nums[left]}, right: {nums[right]}, mid: {nums[mid]}")

            if nums[mid] == target:
                return mid

            # left side
            if nums[left] <= nums[mid]:

                if target > nums[mid] or target < nums[left]:
                    left = mid + 1

                else:
                    right = mid - 1

            # right side nums[mid] <= nums[right]
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1

                else:
                    left = mid + 1

        return -1

        


# I am given a list of numbers with a target value.
# My list of numbers may no longer in order, but there is an order, since the numbers have been rotated.
# Meaning the new list if rotated, would have the frontmost numbers at the rear.
# For example: pre-rotated: [1,2,3,4,5,6] and now if rotated twice: [3,4,5,6,1,2] 

# If the list is rotated:
# Our rightmost value would be less than our leftmost. [3,4,5,6,1,2] -> [5,6,1,2,3,4] -> [6,1,2,3,4,5]. Right is always less than left
# 

# If the list is not rotated:
# Our rightmost value would be greater than our lessmost. [1,2,3,4,5,6]


