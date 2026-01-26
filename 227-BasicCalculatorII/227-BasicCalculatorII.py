# Last updated: 1/26/2026, 1:23:39 AM
1class Solution:
2    def calculate(self, s: str) -> int:
3        stack = []
4        pre_sign = "+"
5        num = 0
6
7        for i, c in enumerate(s):
8            if c.isdigit():
9                num = 10 * num + int(c)
10            if i == len(s) - 1 or c in "+-*/":
11                if pre_sign == "+":
12                    stack.append(num)
13                elif pre_sign == "-":
14                    stack.append(-num)
15                elif pre_sign == "*":
16                    stack.append(stack.pop() * num)
17                elif pre_sign == "/":
18                    stack.append(int(stack.pop() / num))
19
20                pre_sign = c
21                num = 0
22
23        return sum(stack)
24