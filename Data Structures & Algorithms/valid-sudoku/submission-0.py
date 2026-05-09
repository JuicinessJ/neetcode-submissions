class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        # col
        for col in range(len(board)):

            # row
            for row in range(len(board)):

                print(board[col][row])

                if board[col][row].isdigit():
                    if ("row", row, board[col][row]) in seen or \
                        ("col", col, board[col][row]) in seen or \
                        ("box", row//3, col//3, board[col][row]) in seen:
                        return False

                    seen.add(("row", row, board[col][row]))
                    seen.add(("col", col, board[col][row]))
                    seen.add(("box", row//3, col//3, board[col][row]))

        return True
                