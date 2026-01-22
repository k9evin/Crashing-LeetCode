# Last updated: 1/21/2026, 10:39:09 PM
1class Solution:
2    def minimumPairRemoval(self, nums: List[int]) -> int:
3        count = 0
4        flag = False
5
6        while not flag:
7            if nums == sorted(nums):
8                flag = True
9                break
10
11            min_sum = float("inf")
12            target_idx = -1
13
14            for i in range(1, len(nums)):
15                curr_sum = nums[i - 1] + nums[i]
16
17                if curr_sum < min_sum:
18                    min_sum = curr_sum
19                    target_idx = i - 1
20
21            nums[target_idx] = min_sum
22            nums.pop(target_idx + 1)
23            count += 1
24
25        return count
26