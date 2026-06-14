class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        left = 0

        curr_max = 0

        if len(s) <= 1:
            return len(s)

        for right in range(len(s)):

            while s[right] in seen:
                
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            curr_max = max(len(seen), curr_max)

        return curr_max