class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while left < right:
            print(left, right)
            value = (numbers[left] + numbers[right]) - target

            print(value)

            if value > 0:
                right -= 1
            elif value < 0:
                left += 1
            else:
                return [left + 1, right + 1]
        

# I am given a list of numbers in ascending order, in which I need to find two numbers that equals the target value
# I need to return the indices of the two numbers that equal the target

# Since I am proceeding this as a two pointer solution, I will want to create a while loop, that checks if left <= right.
# Where I will increment left or decrement right, until we find the pairs.
# Since this list is ascending order, so i.e: [1,2,3,4], I will increment left if the number is too small, and decrement right if the number is too large.
# Since our recommended time complexity is O(n), we'll be fine with the two pointer approach, but cannot create any storage, since our space complexity is O(1).