# Last updated: 1/3/2026, 10:37:27 PM
1class Solution:
2    def sumFourDivisors(self, nums: List[int]) -> int:
3        total_sum = 0
4
5        for n in nums:
6            count = 0
7            curr_sum = 0
8            for i in range(1, int(n**0.5) + 1):
9                if n % i == 0:
10                    count += 1
11                    curr_sum += i
12
13                    if i * i != n:
14                        count += 1
15                        curr_sum += n // i
16
17                    if count > 4:
18                        break
19
20            if count == 4:
21                total_sum += curr_sum
22
23        return total_sum
24