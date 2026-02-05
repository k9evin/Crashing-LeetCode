# Last updated: 2/4/2026, 9:58:12 PM
1class Solution:
2    def calculate(self, s: str) -> int:
3        stack = []  # Store numbers to be added (after handling */)
4        pre_sign = "+"  # Previous operator
5        num = 0  # Current number being built
6
7        i = 0
8        n = len(s)
9
10        while i < n:
11            c = s[i]
12
13            # Build multi-digit number
14            if c.isdigit():
15                num = num * 10 + int(c)
16
17            # Process when encountering operator or end of string
18            if i == n - 1 or c in "+-*/":
19                if pre_sign == "+":
20                    stack.append(num)  # Addition: push positive
21                elif pre_sign == "-":
22                    stack.append(-num)  # Subtraction: push negative
23                elif pre_sign == "*":
24                    stack.append(
25                        stack.pop() * num
26                    )  # Multiplication: compute immediately
27                elif pre_sign == "/":
28                    # Division: truncate toward zero (not floor division)
29                    stack.append(int(stack.pop() / num))
30
31                pre_sign = c  # Update operator for next processing
32                num = 0  # Reset current number
33
34            i += 1
35
36        # Sum all numbers in stack
37        return sum(stack)
38
39    # Time Complexity: O(n) - single pass through the string
40    # Space Complexity: O(n) - stack may hold up to n/2 numbers in worst case
41