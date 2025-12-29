# Last updated: 12/29/2025, 1:41:01 AM
class Solution:
    def countHomogenous(self, s: str) -> int:
        res = 0
        for _, g in groupby(s):
            n = len(list(g))
            res += n * (n + 1) // 2
        
        return res % (pow(10, 9) + 7)
