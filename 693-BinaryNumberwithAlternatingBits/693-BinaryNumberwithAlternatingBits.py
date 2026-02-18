# Last updated: 2/18/2026, 6:57:39 PM
1class Solution:
2    def hasAlternatingBits(self, n: int) -> bool:
3        # Convert to binary string and remove '0b' prefix
4        bits = bin(n)[2:]
5
6        # Check adjacent bits - they must be different for alternating pattern
7        for i in range(len(bits) - 1):
8            if bits[i] == bits[i + 1]:
9                return False
10
11        return True
12
13
14"""
15Time Complexity: O(1)
16- n is a 32-bit integer, so the binary string has at most 31 characters
17- We iterate through at most 31 characters, which is a constant upper bound
18
19Space Complexity: O(1)
20- We store at most 31 characters for the binary representation
21- The space usage is bounded by a constant (32-bit integer constraint)
22"""
23