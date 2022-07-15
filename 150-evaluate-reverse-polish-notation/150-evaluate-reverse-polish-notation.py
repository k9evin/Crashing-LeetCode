class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Solution 1:
        # Time complexity: O(n)
        # Space complexity: O(n)
        stack = []
        res = 0
        
        for i in tokens:
            try:
                stack.append(int(i))
            except ValueError as e:
                a = stack.pop()
                b = stack.pop()
                match i:
                    case "+":
                        res = a + b
                    case "-":
                        res = b - a
                    case "*":
                        res = a * b
                    case "/":
                        res = int(b / a)
                stack.append(res)
        return stack[-1]
                    
                        
                