class MyQueue:
    
    def __init__(self):
        self.L=[]

    def push(self, x: int) -> None:
        self.L=self.L+[x]

    def pop(self) -> int:
        x=self.L[0]
        self.L=self.L[1:]
        return x
    def peek(self) -> int:
        return self.L[0]

    def empty(self) -> bool:
        if len(self.L)==0:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
