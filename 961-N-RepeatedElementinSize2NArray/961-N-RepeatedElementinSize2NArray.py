# Last updated: 1/1/2026, 11:49:30 PM
1class Solution:
2    def repeatedNTimes(self, nums: List[int]) -> int:
3        # there are n+1 unique elements in a 2n-length array, meaning
4        # exactly one element appears n times and all others appear exactly once.
5        visited = set()
6        for num in nums:
7            if num in visited:  # First repeat must be the n-times element
8                return num
9            visited.add(num)
10
11        # Time: O(n) worst-case, Space: O(n) worst-case
12