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
            




# We are given a matrix list in list, and a target.
# Our matrix's rows are in ascending order, so [1,2,3,4]
# We are asked to find if our target value exist inside our matrix.
# Since a matrix is a list within a list, or nested list, and the values are in ascending order.
# We should start with flattening our matrix into a list, this would make accessing our list, alot simplier.
# However, we are reminded that our space complexity is O(1), meaning we cannot make any supporting data structures.

# Could we use a binary within a binary?
# Since our time complexity constrait is O(log(m * n)), suggesting we may

# The idea would be to first start by checking the first row, if our value is inside, we proceed with the usual.
# If not then we check the next row, and next, until we find our value.
# If we do not find out value we return a False

# To accomplish this:
# We need to first create a outer loop, this maintains the rows, we should use a for loop since its easier and cleaner.
# Inside we create the structure needed to support the while loop.
# Nothing here will be different.



