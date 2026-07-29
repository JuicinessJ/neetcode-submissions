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