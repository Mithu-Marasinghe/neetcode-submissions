class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value = float("inf")

    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append(val - self.min_value)
            if (val < self.min_value):
                self.min_value = val
        else:
            self.stack.append(0)
            self.min_value = val

    def pop(self) -> None:
        if not self.stack:
            return 
        
        last_val = self.stack.pop()
        if last_val < 0:
            self.min_value = self.min_value - last_val

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.min_value
        else:
            return int(self.min_value)

    def getMin(self) -> int:
        return int(self.min_value)
