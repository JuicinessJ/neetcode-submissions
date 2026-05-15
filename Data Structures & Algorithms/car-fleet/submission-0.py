class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[pos, speed] for pos, speed in zip(position, speed)]

        stk = []

        for pos, speed in sorted(pair)[::-1]:
            stk.append((target - pos) / speed)

            if len(stk) >= 2 and stk[-1] <= stk[-2]:
                stk.pop()

        return len(stk)
        


