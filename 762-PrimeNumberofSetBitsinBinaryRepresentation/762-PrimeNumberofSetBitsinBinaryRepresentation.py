# Last updated: 2/21/2026, 6:35:35 PM
1class Solution:
2    def countPrimeSetBits(self, left: int, right: int) -> int:
3        res = 0
4        prime = {2, 3, 5, 7, 11, 13, 17, 19}
5        for n in range(left, right + 1):
6            bin_n = bin(n)
7            set_count = bin_n.count("1")
8            if set_count in prime:
9                res += 1
10
11        return res
12