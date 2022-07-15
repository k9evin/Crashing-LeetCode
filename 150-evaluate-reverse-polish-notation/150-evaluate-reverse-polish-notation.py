class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Solution 1:
        # Time complexity: O(n)
        # Space complexity: O(n)
#         stack = []
#         res = 0
        
#         for i in tokens:
#             try:
#                 stack.append(int(i))
#             except ValueError as e:
#                 a = stack.pop()
#                 b = stack.pop()
#                 match i:
#                     case "+":
#                         res = a + b
#                     case "-":
#                         # the order matters!
#                         res = b - a
#                     case "*":
#                         res = a * b
#                     case "/":
#                         # be careful with the division operator
#                         res = int(b / a)
#                 stack.append(res)
#         return stack[-1]
    
        # Solution 2:
        # Time complexity: O(n)
        # Space complexity: O(n)
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        return stack[0]
                    
                        
                