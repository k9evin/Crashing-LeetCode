# Last updated: 2/17/2026, 5:42:38 PM
1class Solution:
2    def readBinaryWatch(self, turnedOn: int) -> List[str]:
3        ans = list()
4        for h in range(12):
5            for m in range(60):
6                if bin(h).count("1") + bin(m).count("1") == turnedOn:
7                    ans.append(f"{h}:{m:02d}")
8        return ans
9