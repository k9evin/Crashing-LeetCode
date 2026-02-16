# Last updated: 2/16/2026, 6:34:21 PM
1class Solution:
2    def reverseBits(self, n: int) -> int:
3        # Initialize result
4        res = 0 
5
6        # Loop for each bit
7        for _ in range(32):  
8            # Shift res to the left by 1 bit and perform bitwise OR with the last bit of n
9            res = (res << 1) | (n & 1)
10            # Shift n to the right by 1 bit
11            n >>= 1 
12        
13        return res