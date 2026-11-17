class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for num in nums:
            if num not in seen:
                seen[num] = 0

            seen[num] += 1

        arr = []

        for key, val in seen.items():
            arr.append([val, key])
        arr.sort()

        res = []

        while len(res) < k:
            res.append(arr.pop()[1])

        return res