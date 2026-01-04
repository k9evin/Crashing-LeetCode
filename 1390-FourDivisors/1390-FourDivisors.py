# Last updated: 1/3/2026, 11:01:59 PM
1class Solution:
2    def sumFourDivisors(self, nums: List[int]) -> int:
3        total_sum = 0  # T: O(1), S: O(1)
4
5        for n in nums:  # T: O(N), where N = len(nums)
6            count = 0
7            curr_sum = 0
8            # Iterate up to sqrt(n) to find divisors
9            for i in range(1, int(n**0.5) + 1):  # T: O(sqrt(n)) per number
10                if n % i == 0:
11                    count += 1
12                    curr_sum += i
13
14                    if i * i != n:  # Avoid double-counting perfect squares
15                        count += 1
16                        curr_sum += n // i
17
18                    if count > 4:  # Early exit if more than 4 divisors
19                        break
20
21            if count == 4:  # Only add if exactly 4 divisors
22                total_sum += curr_sum
23
24        return total_sum  # Overall T: O(N * sqrt(M)), S: O(1), M = max(nums)