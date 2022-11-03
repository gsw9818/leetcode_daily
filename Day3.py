class CustomStack:

    def __init__(self, maxSize: int):
        self.CustomStack = [0]*maxSize
        self.top = -1 #栈顶为-1，表示栈空

    def push(self, x: int) -> None:
        if self.top != len(self.CustomStack) - 1:#栈顶为总长度-1，表示栈满
            self.top += 1
            self.CustomStack[self.top] = x
        
    def pop(self) -> int:
        if self.top == -1:
            return -1
        self.top -= 1
        return self.CustomStack[self.top+1]

    def increment(self, k: int, val: int) -> None:
        for i in range( min( (k) , self.top + 1 ) ):
            self.CustomStack[i] += val




# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
