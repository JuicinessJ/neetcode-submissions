class MinStack:

    def __init__(self):
        self.stk = []
        self.min_stk = []
        
    def push(self, val: int) -> None:
        self.stk.append(val)

        if len(self.min_stk) == 0:
            self.min_stk.append(val)
        else:
            if val < self.min_stk[-1]:
                self.min_stk.append(val)
            else:
                self.min_stk.append(self.min_stk[-1])

    def pop(self) -> None:
        self.stk.pop()
        self.min_stk.pop()
        
    def top(self) -> int:
        return self.stk[-1]
        

    def getMin(self) -> int:
        return self.min_stk[-1]
        


# I am tasked to create a MinStack class, where I need to declare 4 features, a push, pop, tp, and getMin.
# Push, pop, top, are self-explatory, where I can use Python features to accomplish.
# However, I need to deteremine how I want to proceed with accomplishing getMin.
# getMin needs be a solution to return a O(1) time and O(n) for space. 
# To accomplish this, I will need to create an active history, that tracks the active min.
# However, how would this work


        
