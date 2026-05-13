class Solution:
    def isValid(self, s: str) -> bool:
        map = {")": "(", "}": "{", "]": "["}
        stk = []

        if len(s) <= 1:
            return False

        for c in s:

            if c in map and len(stk) == 0:
                return False

            if c in map:

                pop = stk.pop()

                if map[c] != pop:
                    return False
                
            else:
                stk.append(c)

        if len(stk) != 0:
            return False
            
        return True