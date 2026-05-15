class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[pos, speed] for pos, speed in zip(position, speed)]

        stk = []

        for pos, speed in sorted(pair)[::-1]:
            stk.append((target - pos) / speed)

            if len(stk) >= 2 and stk[-1] <= stk[-2]:
                stk.pop()

        return len(stk)
        

# Zips together position and speed, so when we sort by positon, we do not lose the association of speed
# We iterate through the pair, in reversed sorted order, so descending. With positon greatest to smallest
# We append every pair into the stack regardless of their value, but once our stack has become a size of 2 or greater
# We start comparing the newest value, and the previous newest value, and check if the "oldest" is greater or equal to our new value
# If true, we pop, since when we sorted by positon, every car behind in position is bottlenecked by our leading car, regardless of their speed.
# So if our newest value, which would be behind, the leading car, it'll have to either match the leading car speed, or is slower.
# If slower, we do nothing, and have a new independent fleet, if faster, than we pop, since our leading car remains the leading car
# If slower, than this newest car would be the new bottleneck, and all trailing car must match their speed too.
# Then we return the size of the stack, representing the number of car fleets


