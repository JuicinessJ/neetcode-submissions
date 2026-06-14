class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        left = 0

        curr_max = 0

        if len(s) <= 1:
            return len(s)

        for right in range(len(s)):

            print(left, right, seen)

            print(f"Adding from right: {s[right]}")

            while s[right] in seen:
                
                print(f"Removing from left: {s[left]}")
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            curr_max = max(len(seen), curr_max)

        return curr_max


        

# I am given a string, and need to find the longest substring wothout a repeating character.
# I then will need to return the length of the substring.

# To accomplish this, I should try a two-pointer/sliding window solution.
# I am also asked to obide with O(n) for time, and O(m) where m is the unique characters of n for space.

# Meaning, I am asked to use only 1 loop.
# I will utilize keeping track of our left and right indexes.
# While we are incrementing the sliding window to include a substring.
# I will check if the new character == our left index.
# If it does ==, I should increment left and continue.
# However, there are chances where the repeating chars are not the left value, but perhaps in-between.
# Since this is essentially asking if there are duplicate, I should use a set.
# Where as we increment right, we add the new values into the set.
# But if the value already exist, and the value isn't left index, then we stop there returning the length of the set.
# Or we reset the window, recording the currently longest substring assuming we could make a new one.