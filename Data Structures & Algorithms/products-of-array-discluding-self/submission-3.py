class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_lst = [1] * len(nums)
        suf_lst = [1] * len(nums)

        for i in range(1, len(nums)):
            pre_lst[i] = nums[i - 1] * pre_lst[i - 1]
            suf_lst[-i - 1] = nums[-i] * suf_lst[-i]

        print(suf_lst)

        new_lst = [1] * len(nums)

        for i in range(len(nums)):
            new_lst[i] = pre_lst[i] * suf_lst[i]

        return new_lst


        