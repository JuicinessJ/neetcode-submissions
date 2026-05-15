class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for row in matrix:

            low = 0
            high = len(row) - 1

            while low <= high:

                mid = low + (high - low) // 2

                val = row[mid]

                if val < target:
                    low = mid + 1
                
                elif val > target:
                    high = mid - 1

                else:
                    return True

        return False


