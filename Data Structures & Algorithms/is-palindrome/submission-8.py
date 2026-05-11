class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = "".join(c.lower() for c in s if c.isalnum()) # extract c if is chars or numbers

        left = 0
        right = len(new_s) - 1

        while left <= right:

            if new_s[left] != new_s[right]:
                return False

            left += 1
            right -= 1
            
        return True