class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = max_len = 0
        window = set()

        for right in range(len(s)):

            while s[right] in window:
                window.remove(s[left])
                left += 1

            window.add(s[right])

            curr_len = len(window)

            if max_len < curr_len:
                max_len = curr_len
        
        return max_len





# Input: string of characters
# Output: number representing length of substring w/o repeating characters

# We are asked to find a substring w/o repeating characters, we know this will utilize a sliding window approach, where our right pointer continue traversing, but we bring our left pointer forward if s[right] remains in this window. 

# This means we could use a hashset, since we are looking for exclusive, however, hashset utilize O(1) methods of adding and removing.
# Creating a problem, where it doesn't rely on window, and would remove the 