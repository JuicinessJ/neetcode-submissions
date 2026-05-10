class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums) # creates the set

        longest_seq = 0

        for num in seen:
            length = 1
            if num - 1 not in seen: # current num is smallest
                while (num + 1) in seen: # increment count until num isn't in seen
                    num += 1
                    length += 1

                if length > longest_seq:
                    longest_seq = length

        return longest_seq





