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

            print(stk)
                
        return int(stk[-1])

# I am given a list of tokens, which represent numbers and operators
# I need to return the sum of the values with their operators

# Since I am pursuing as a stack approach, I will want to iterate through the list, and append every number into the stack
# If I encounter an operator, I will want to pop the top two values and use them with their operator.
# Afterwards, I will want to append them back into their stk and continue the process.
# Returning the last value inside the stack by [-1]
        