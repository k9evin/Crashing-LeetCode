# Last updated: 2/16/2026, 6:31:03 PM
1class Solution:
2    def addBinary(self, a: str, b: str) -> str:
3        n = max(len(a), len(b))
4        a, b = a.zfill(n), b.zfill(n)
5
6        carry = 0
7        answer = []
8        for i in range(n - 1, -1, -1):
9            if a[i] == "1":
10                carry += 1
11            if b[i] == "1":
12                carry += 1
13
14            if carry % 2 == 1:
15                answer.append("1")
16            else:
17                answer.append("0")
18
19            carry //= 2
20
21        if carry == 1:
22            answer.append("1")
23        answer.reverse()
24
25        return "".join(answer)
26