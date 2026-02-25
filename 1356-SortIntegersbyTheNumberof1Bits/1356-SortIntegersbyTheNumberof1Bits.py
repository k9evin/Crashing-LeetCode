# Last updated: 2/25/2026, 6:01:55 PM
1class Solution:
2    def sortByBits(self, arr: List[int]) -> List[int]:
3        def hammingWeight(n: int) -> int:
4            count = 0
5
6            while n:
7                # n & (n-1) will remove the rightmost 1 in binary representation of n
8                n = n & (n - 1)
9                count += 1
10
11            return count
12
13        arr.sort(key=lambda n: (hammingWeight(n), n))
14        return arr
15