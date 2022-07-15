class MinStack:
    
    # Your MinStack object will be instantiated and called as such:
    # obj = MinStack()
    # obj.push(val)
    # obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.getMin()

    # Solution 1:
    # Time complexity: O(1)
    # Space complexity: O(n)
        
#     def __init__(self):
#         self.stack = []
#         self.min = []

#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         if not self.min:
#             self.min.append(val)
#         else:
#             self.min.append(min(self.min[-1], val))

#     def pop(self) -> None:
#         if self.stack:
#             self.stack.pop()
#             self.min.pop()

#     def top(self) -> int:
#         if self.stack:
#             return self.stack[-1]

#     def getMin(self) -> int:
#         return self.min[-1]
    
    # Solution 2:
    # Time complexity: O(1)
    # Space complexity: O(n)
    
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # append a pair of val and the minimum element
        self.stack.append((val, min(val, self.stack[-1][1] if self.stack else val)))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]