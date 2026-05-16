class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        best_time = right

        while left <= right:

            k = (left + right) // 2

            total_time = 0

            for p in piles:

                total_time += math.ceil(p / k)

            if total_time <= h:

                best_time = min(best_time, k)
                right = k - 1

            else:

                left = k + 1

        return best_time

