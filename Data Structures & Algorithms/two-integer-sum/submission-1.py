class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # map of seen nums

        # extrapolate the index and numerical value from list
        for i, num in enumerate(nums):

            # finds the value we need from subtracting target from current value from list
            value = target - num

            # if value is in map
            if value in seen:
                return [seen[value], i] # return index of value, and current index

            seen[num] = i # adds index to key of num


            