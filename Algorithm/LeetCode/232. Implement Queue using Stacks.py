# 스택을 사용하여 큐를 구현하는 문제

"""
1. push할 때 사용하는 inStack과 pop할 때 사용하는 outStack을 생성합니다.
2. push일 경우에는 무조건 inStack에 데이터를 append합니다.
3. pop일 경우에 outStack에 아무 데이터가 없을 경우, inStack에 있는 모든 데이터를 pop한 후, outStack에 append합니다. 
-> 이를 진행할 경우, inStack에 있던 모든 데이터들이 거꾸로 outStack에 저장되어 가장 먼저 들어온 데이터가 pop 됩니다.
3-1. pop인데 outStack에 이미 데이터가 있다면 그대로 끝 데이터인 pop을 진행합니다.
"""

class MyQueue:
    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, x: int) -> None:
        self.inStack.append(x)

    def pop(self) -> int:
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack.pop()

    def peek(self) -> int:
        if not self.outStack:
            return self.inStack[0]
        else:
            return self.outStack[-1]

    def empty(self) -> bool:
        if self.inStack or self.outStack:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()