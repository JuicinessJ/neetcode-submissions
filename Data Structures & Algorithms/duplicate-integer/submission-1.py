class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_map = []

        for num in nums:
            if num in dup_map:
                return True
            else:
                dup_map.append(num)
        
        return False

