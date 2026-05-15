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