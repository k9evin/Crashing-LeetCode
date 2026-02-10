# Last updated: 2/10/2026, 6:46:34 PM
1class Solution:
2    def longestBalanced(self, nums: List[int]) -> int:
3        max_len = 0
4
5        for i in range(len(nums)):
6            even = set()
7            odd = set()
8
9            for j in range(i, len(nums)):
10                if nums[j] % 2 == 0:
11                    even.add(nums[j])
12                else:
13                    odd.add(nums[j])
14
15                if len(even) == len(odd):
16                    max_len = max(max_len, j - i + 1)
17
18        return max_len
19