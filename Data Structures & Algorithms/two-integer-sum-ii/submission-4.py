class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while left < right:
            value = (numbers[left] + numbers[right]) - target
            
            if value > 0:
                right -= 1
            elif value < 0:
                left += 1
            else:
                return [left + 1, right + 1]