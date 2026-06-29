class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = {}
        longest_substring = 0

        for right in range(len(s)):
            if s[right] not in freq:
                freq[s[right]] = 0

            freq[s[right]] += 1
            
            if (right - left + 1) - max(freq.values()) > k:
                freq[s[left]] -= 1
                left += 1

            longest_substring = max(longest_substring, right - left + 1)

        return longest_substring
