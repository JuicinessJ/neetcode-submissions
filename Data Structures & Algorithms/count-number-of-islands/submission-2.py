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