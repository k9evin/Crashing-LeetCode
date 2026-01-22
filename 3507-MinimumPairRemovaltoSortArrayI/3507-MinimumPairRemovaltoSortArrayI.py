# Last updated: 1/21/2026, 10:34:59 PM
1class Solution:
2    def minimumPairRemoval(self, nums: List[int]) -> int:
3        count = 0
4
5        while len(nums) > 1:
6            if nums == sorted(nums):
7                break
8
9            min_sum = float("inf")
10            target_idx = -1
11
12            for i in range(1, len(nums)):
13                curr_sum = nums[i - 1] + nums[i]
14
15                if curr_sum < min_sum:
16                    min_sum = curr_sum
17                    target_idx = i - 1
18
19            nums[target_idx] = min_sum
20            nums.pop(target_idx + 1)
21            count += 1
22
23        return count
24