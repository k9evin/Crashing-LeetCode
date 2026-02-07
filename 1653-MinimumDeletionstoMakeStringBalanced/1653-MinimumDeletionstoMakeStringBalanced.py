# Last updated: 2/7/2026, 4:47:08 PM
1class Solution:
2    def minimumDeletions(self, s: str) -> int:
3        n = len(s)
4        count_a = [0] * n
5        count_b = [0] * n
6        b_count = 0
7
8        # First pass: compute count_b which stores the number of
9        # 'b' characters to the left of the current position.
10        for i in range(n):
11            count_b[i] = b_count
12            if s[i] == "b":
13                b_count += 1
14
15        a_count = 0
16        # Second pass: compute count_a which stores the number of
17        # 'a' characters to the right of the current position
18        for i in range(n - 1, -1, -1):
19            count_a[i] = a_count
20            if s[i] == "a":
21                a_count += 1
22
23        min_deletions = n
24        # Third pass: iterate through the string to find the minimum deletions
25        for i in range(n):
26            min_deletions = min(min_deletions, count_a[i] + count_b[i])
27        return min_deletions