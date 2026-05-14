class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stk = []

        for i, temp in enumerate(temperatures):

            while stk and stk[-1][0] < temp:

                stk_temp, stk_index = stk.pop()

                res[stk_index] = i - stk_index

            stk.append([temp, i])

        return res