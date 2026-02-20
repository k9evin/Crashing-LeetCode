# Last updated: 2/20/2026, 6:45:29 PM
1class Solution:
2    def makeLargestSpecial(self, s: str) -> str:
3        count = i = 0
4        res = []
5        for j, v in enumerate(s):
6            count = count + 1 if v == "1" else count - 1
7            if count == 0:
8                res.append("1" + self.makeLargestSpecial(s[i + 1 : j]) + "0")
9                i = j + 1
10        return "".join(sorted(res)[::-1])
11