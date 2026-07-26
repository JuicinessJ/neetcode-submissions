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

        

"""
I am given a board and a word, I need to locate if this word exist within the board.
However, the characters must be connected when forming.
Meaning, as we iterate through the word, each letters following must be touching.
Whether that is above, below, to the left, or right.

To discover if the word exist, I should start with iterating through the board, top down.
If we discover the first letter of our word, we should stop iterating top down, left to right.
And start to compare its neighbors.
However, what if the word is spelt in reverse order, where our last letter is at the top and our first letter is at the bottom.
Or perhaps right to left...

Instead, of checking for the first letter, we should just check if a letter within a word exist.
If it does we immediately compare the neighbors.

But how does this work with a backtracking approach?
Our base case needs to be a condition that returns true for us to stop traversing, and to start backtracking neighbors.

What if we search for the last letter, but this would be an issue if our word is spelt in reverse order too.
Assuming we make our base case to be if index of letter == leters in word...
Since the base case would stop the recursion, and start backtracking.

The base case stops tracking and starts backtracking...

So to start this while using the backtrack.
Our backtrack will take 2 params, i and j.
i and j are the index of board.

Our goal, isn't to decide if we add or don't add.
Instead is to find if the index of letter == letters in word.
So we should start with hashing our word.
If the word exist, we immediately start comparing neighbors.
If it doesn't exist, we do nothing and continue trarversing.

If we find a letter that exist, we add the indexes into our result list.
If the length of result == len of word, we return True

"""