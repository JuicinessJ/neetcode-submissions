class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        map = {}

        # Anagrams are words that share the same count, regardless of order
        # use dictionary, mapping each word sorted by key, and storing word unsorted as value.
        # ie act => act, and cat => act, so {"act": ["act", "cat"]}...

        for word in strs:
            sort = sorted(word)
            sort = "".join(sort)

            if sort not in map:
                map[sort] = []
            
            map[sort].append(word)

        return list(map.values())