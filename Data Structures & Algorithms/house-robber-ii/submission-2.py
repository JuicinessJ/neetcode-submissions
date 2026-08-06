class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp_first = [0] * (len(nums) + 1)
        dp_first[0] = nums[0]
        dp_first[1] = max(nums[0], nums[1])

        for i in range(2, len(nums) - 1):
            dp_first[i] = max(nums[i] + dp_first[i - 2], dp_first[i - 1])

        dp_second = [0] * (len(nums) + 1)
        dp_second[0] = 0
        dp_second[1] = nums[1]

        for i in range(2, len(nums)):
            dp_second[i] = max(nums[i] + dp_second[i - 2], dp_second[i - 1])

        return max(dp_first[len(nums) - 2], dp_second[len(nums) - 1])