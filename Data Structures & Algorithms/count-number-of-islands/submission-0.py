class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        total = 0

        def dfs(i, j):

            if i < 0 or j < 0 or i >= row or j >= col:
                return

            if grid[i][j] != "1":
                return False

            

            grid[i][j] = "0"

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j -1)


        for j in range(col):
            for i in range(row):
                if grid[i][j] == "1":
                    total += 1
                    dfs(i, j)

        return total
        

"""
I am given a matrix, and asked to return the number of "islands" we can form.
Each island is created by connecting or adjacent lands horizontally, or vertically.
Where each island is surrounded by water.
I am asked to return the unique number of islands we can create.

To determine how many islands we can create, we need to determine how we would traverse this matrix
We could traverse the matrix as usual, where we traverse row by row.
However, how would we connect the ones from different rows.
We could compare their index, if their index are connected we return as the same island.

However, how would we increment the total of islands.
We could increment each time our island disconnect when traversing row by row.
But what if an island reconnect on a different row.
This would interfer with our basic incrementing.
In addition, what happens when we enter a new row, would this incrementing also increment a cell that may be connected?

We could try a backtrack problem similar to word search.
By calling backtrack function and passing the index where we found a starting island.

But how would we have it take new index, and how would we know if the previous indices given were connected?


"""