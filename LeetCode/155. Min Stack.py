class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # 현재 들어오는 값과 minStack의 마지막값을 비교하여 작은 값을 push한다. 데이터 pop을 하더라도 가장 작은 값이 사라질 때, minStack에서는 다음으로 가장 작은 값이 들어있으므로 상관없다.
        if len(self.minStack) > 0:
            self.minStack.append(min(val, self.minStack[-1]))
        else:
            self.minStack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]