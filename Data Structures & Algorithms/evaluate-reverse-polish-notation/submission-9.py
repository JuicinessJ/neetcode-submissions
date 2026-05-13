class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "-", "*", "/"]
        stk = []

        for t in tokens:

            sum = 0

            if t in ops:

                val1 = stk.pop()
                val2 = stk.pop()

                if t == "+":
                    sum += int(val2) + int(val1)

                if t == "-":
                    sum += int(val2) - int(val1)

                if t == "*":
                    sum += int(val2) * int(val1)

                if t == "/":
                    sum += int(val2) / int(val1)

                stk.append(sum)

            else:
                stk.append(t)
                
        return int(stk[-1])
        