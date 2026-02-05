# Last updated: 2/4/2026, 11:57:48 PM
1class Solution:
2    def calculate(self, s: str) -> int:
3        def helper(i):
4            stack = []
5            pre_sign = "+"
6            num = 0
7            n = len(s)
8
9            while i < n:
10                c = s[i]
11
12                if c.isdigit():
13                    num = num * 10 + int(c)
14
15                if c == "(":
16                    num, i = helper(i + 1)
17
18                if i == n - 1 or c in "+-*/)":
19                    if pre_sign == "+":
20                        stack.append(num)
21                    elif pre_sign == "-":
22                        stack.append(-num)
23                    elif pre_sign == "*":
24                        stack.append(stack.pop() * num)
25                    elif pre_sign == "/":
26                        stack.append(int(stack.pop() / num))
27
28                    pre_sign = c
29                    num = 0
30
31                    if c == ")":
32                        return sum(stack), i
33
34                i += 1
35
36            return sum(stack), i
37
38        res, _ = helper(0)
39        return res
40