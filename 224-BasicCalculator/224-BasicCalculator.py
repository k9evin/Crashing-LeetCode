# Last updated: 2/4/2026, 11:45:44 PM
1class Solution:
2    def calculate(self, s: str) -> int:
3        def helper(i):
4            # Recursive helper to process expression starting at index i
5            stack = []          # Store numbers to be added (handles nested expressions)
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
21                # Process when encountering operator, closing parenthesis, or end
22                if i == n - 1 or c in "+-)":
23                    # Apply previous operator to current number
24                    if pre_sign == "+":
25                        stack.append(num)      # Addition
26                    elif pre_sign == "-":
27                        stack.append(-num)     # Subtraction (or unary minus)
28
29                    pre_sign = c               # Update operator for next number
30                    num = 0                    # Reset current number
31
32                    # Return when encountering closing parenthesis
33                    if c == ")":
34                        return sum(stack), i   # Return result and current index
35
36                i += 1
37
38            # Return result for non-parenthesized expression or main call
39            return sum(stack), i
40
41        # Start recursive evaluation from index 0
42        res, _ = helper(0)
43        return res
44
45# Time Complexity: O(n) - each character processed once, recursive calls process each character once
46# Space Complexity: O(n) - recursion stack depth up to n in worst case (deeply nested parentheses)