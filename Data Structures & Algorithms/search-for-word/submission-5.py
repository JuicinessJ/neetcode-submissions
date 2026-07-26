class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        row = len(board)
        col = len(board[0])
        idx = 0

        def backtrack(i, j, idx):

            if idx == len(word):
                return True

            if (i, j) in visited:
                return False

            # Index larger than dimension of board
            if (i >= row or j >= col or i < 0 or j < 0):
                return False

            # If cell != letter, backtrack
            if board[i][j] != word[idx]:
                return False

            visited.add((i,j))

            res = (backtrack(i + 1, j, idx + 1) or
                backtrack(i - 1, j, idx + 1) or
                backtrack(i, j + 1, idx + 1) or
                backtrack(i, j - 1, idx + 1))

            visited.remove((i,j))

            return res

        for i in range(row):
            for j in range(col):

                if backtrack(i, j, idx):
                    return True

        return False