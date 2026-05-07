class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}

        for num in nums:
            if num not in map:
                map[num] = 0
            map[num] += 1

        return [key for key, v in sorted(map.items(), reverse=True, key=lambda x: x[1])][:k]