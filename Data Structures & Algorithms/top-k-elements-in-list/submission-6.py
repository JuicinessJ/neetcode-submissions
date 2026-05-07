class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}

        for num in nums:
            if num not in map:
                map[num] = 0
            map[num] += 1
        return [key for key, value in sorted(map.items(), reverse=True, key=lambda x: x[1])][:k]
        # .items()... gets (key, value)
        # reverse=True... sort by descending order, most frequent k
        # key=lambda x: x[1]... passes in value to be sorted instead of key(x[0])
        # [:k]... splice list from 0 to k
        # key for key, value in... unpacks tuple (key, value) and only return key variable, discarding value