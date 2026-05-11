class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        seen = set()

        for base in range(len(nums) - 1):

            left = base + 1
            right = len(nums) - 1

            while left < right:

                target = nums[base] + nums[left] + nums[right]

                if target < 0:
                    left += 1
                elif target > 0:
                    right -=1
                else:
                    seen.add((nums[base], nums[left], nums[right]))
                    left += 1
                    right -= 1

        return [list(trip) for trip in seen]

