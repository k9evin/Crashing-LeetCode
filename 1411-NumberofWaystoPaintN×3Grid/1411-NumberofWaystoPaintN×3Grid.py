# Last updated: 1/3/2026, 3:17:33 AM
1class Solution:
2    def numOfWays(self, n: int) -> int:
3        # MOD constant for large number handling as required by the problem
4        MOD = 10**9 + 7
5
6        # A represents the number of ways to paint a row in ABA pattern
7        # (first and third cells have the same color)
8        # B represents the number of ways to paint a row in ABC pattern
9        # (all three cells have different colors)
10        # For n = 1, there are 6 ways for each pattern (total 12)
11        A = B = 6
12
13        # Iterate from the second row to the nth row
14        # Update the counts based on valid transitions between patterns:
15        # - Each ABA pattern can be followed by 2 ABA and 2 ABC patterns
16        # - Each ABC pattern can be followed by 2 ABA and 3 ABC patterns
17        for _ in range(2, n + 1):
18            A, B = (2 * A + 2 * B) % MOD, (2 * A + 3 * B) % MOD
19
20        # Return total number of valid configurations modulo MOD
21        return (A + B) % MOD
22
23        # Time Complexity: O(n) - single loop from 2 to n
24        # Space Complexity: O(1) - only using two variables A and B
25