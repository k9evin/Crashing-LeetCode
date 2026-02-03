# Last updated: 2/3/2026, 6:59:13 PM
1class Solution:
2    def isTrionic(self, nums: List[int]) -> bool:
3        count = 1
4        is_increasing = True
5        p = -1
6        q = -1
7
8        for i in range(1, len(nums)):
9            if nums[i - 1] < nums[i]:
10                if not is_increasing:
11                    is_increasing = True
12                    count += 1
13                    q = i - 1
14            elif nums[i - 1] > nums[i]:
15                if is_increasing:
16                    is_increasing = False
17                    count += 1
18                    p = i - 1
19            else:
20                return False
21
22        return is_increasing and count == 3 and p > 0 and p < q and q < (len(nums) - 1)
23