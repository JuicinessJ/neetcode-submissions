class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        # Edge Case: s and t must = in length
        if len(s) != len(t):
            return False

        l = len(s) # length

        for i in range(l):
            if s[i] not in s_map:
                s_map[s[i]] = 0
            s_map[s[i]] += 1

            if t[i] not in t_map:
                t_map[t[i]] = 0
            t_map[t[i]] += 1

        if s_map == t_map:
            return True
        else:
            return False

        



