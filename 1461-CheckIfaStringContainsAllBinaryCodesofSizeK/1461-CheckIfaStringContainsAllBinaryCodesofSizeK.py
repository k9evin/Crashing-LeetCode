# Last updated: 2/23/2026, 6:24:25 PM
1class Solution:
2    def hasAllCodes(self, s: str, k: int) -> bool:
3        need = 1 << k
4        got = set()
5
6        for i in range(k, len(s) + 1):
7            tmp = s[i - k : i]
8            if tmp not in got:
9                got.add(tmp)
10                need -= 1
11                # return True when found all occurrences
12                if need == 0:
13                    return True
14        return False
15