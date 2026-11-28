class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        pair = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for c in s:
            if c in pair:
                if len(stk) == 0:
                    return False

                popped = stk.pop()

                if pair[c] != popped:
                    return False
            
            else:
                stk.append(c)


        if len(stk) == 0:
            return True

        return False

            

# Input: string of characters, each a bracket
# Output: boolean if brackets given are valid, as in each close has an open, and in the correct order.

# Read each character, append each character onto stack, unless character is a closing.
# If character is closing, pop from stack and compare if pair is valid.
# If valid, continue reading next character
# If not valid, return False