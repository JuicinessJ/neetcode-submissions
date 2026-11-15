class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def count(s: str):
            freq = {}

            for c in s:
                if c not in freq:
                    freq[c] = 0

                freq[c] += 1

            return freq

        return count(s) == count(t)


