# Last updated: 2/5/2026, 12:02:29 AM
1class Solution:
2    def calculate(self, s: str) -> int:
3        def helper(i):
4            # Recursive helper to process expression starting at index i
5            stack = []          # Store numbers to be added (handles */ priority)
6            pre_sign = "+"      # Previous operator before current number
7            num = 0             # Current number being built
8            n = len(s)
9
10            while i < n:
11                c = s[i]
12
13                # Build multi-digit number
14                if c.isdigit():
15                    num = num * 10 + int(c)
16
17                # Handle opening parenthesis: recursively evaluate sub-expression
18                if c == "(":
19                    num, i = helper(i + 1)  # num gets result, i gets updated index
20
21                # Process when encountering operator, ')', or end of string
22                if i == n - 1 or c in "+-*/)":
23                    # Apply previous operator to current number
24                    if pre_sign == "+":
25                        stack.append(num)               # Addition
26                    elif pre_sign == "-":
27                        stack.append(-num)              # Subtraction (or unary minus)
28                    elif pre_sign == "*":
29                        stack.append(stack.pop() * num) # Multiplication: compute immediately
30                    elif pre_sign == "/":
31                        # Division: truncate toward zero (not floor division)
32                        stack.append(int(stack.pop() / num))
33
34                    pre_sign = c  # Update operator for next number
35                    num = 0       # Reset current number
36
37                    # Return when encountering closing parenthesis
38                    if c == ")":
39                        return sum(stack), i  # Return result and current index
40
41                i += 1
42
43            # Return result for current expression level
44            return sum(stack), i
45
46        # Start recursive evaluation from index 0
47        res, _ = helper(0)
48        return res
49
50# Time Complexity: O(n) - each character processed once, recursive calls process each character once
51# Space Complexity: O(n) - recursion stack depth up to n in worst case (deeply nested parentheses)