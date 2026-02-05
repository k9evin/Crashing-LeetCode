# Last updated: 2/5/2026, 6:27:51 PM
1class Solution:
2    def constructTransformedArray(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        res = [0] * n
5
6        for i, num in enumerate(nums):
7            if num > 0:
8                res[i] = nums[(i + num) % n]
9            elif num < 0:
10                res[i] = nums[(i - abs(num) + n) % n]
11            else:
12                res[i] = num
13
14        return res
15