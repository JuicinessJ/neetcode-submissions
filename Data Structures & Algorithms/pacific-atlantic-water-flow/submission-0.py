class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        atlantic, pacific = set(), set()

        def dfs(i, j, ocean, prev_height):
            if i < 0 or j < 0 or i >= row or j >= col:
                return

            if (i,j) in ocean:
                return

            if heights[i][j] < prev_height:
                return

            ocean.add((i, j))

            dfs(i + 1, j, ocean, heights[i][j])
            dfs(i - 1, j, ocean, heights[i][j])
            dfs(i, j + 1, ocean, heights[i][j])
            dfs(i, j - 1, ocean, heights[i][j])

        # iterate through columns
        for j in range(col):
            dfs(0, j, pacific, heights[0][j])
            dfs(row - 1, j, atlantic, heights[row - 1][j])

        # iterate through rows
        for i in range(row):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, col - 1, atlantic, heights[i] [col - 1])

        res = []
        for r in range(row):
            for c in range(col):

                if (r, c) in atlantic and (r, c) in pacific:
                    res.append([r, c])

        return res




        

"""
I am given a integer matrix, each cell representing their height above sea level.
I am asked to return a list of indices, or cells, where water from one ocean, can reach another.
However, instead of a single path, I am asked for all cells that can meet the criteria.

This criteria is: from the cell we choose to start from at one ocean,
the neighboring cells must be less than in height.
However, for the cells to matter, or be considered, they must either lead,
or touch a different ocean.

This means that we will need to find the cell in either ocean, that are less than or equal,
to the starting cell we choose, depending on which ocean we start with.

We could start with traversing through the entire matrix, and looking for equal values, or a max and min value.
We could store these max and min values in a hashmap, where the value is the key, and the indices are the value within the hashmap.
While also maintaining an active pointer that keeps track of the max and min values.

So when we finish traversing we can reference to what are the max and min values.
However, this may be inefficient and another problem, how how would we traverse from the indices, 
without checking if the neighboring cells meet our criteria.

Perhaps, we could try a backtracking approach, where we first build the tree of possibilities.
Then recursively repeat each set of indices.

Or perhaps, when we first run the algo, we take the first index [0, 0].
And try neighboring cells to see if the criteria is met, if not, we try a new cell, and repeat.
But this again, is also expensive, but meets the O(n*m) time complexity.




"""