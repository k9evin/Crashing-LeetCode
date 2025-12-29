# Last updated: 12/29/2025, 2:50:31 AM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        l, r = 0, len(nums) - 1
4
5        while l <= r:
6            m = l + (r - l) // 2
7            if nums[m] == target:
8                return m
9            # Check if left half is sorted
10            if nums[l] <= nums[m]:
11                # Target is in the sorted left half
12                if nums[l] <= target < nums[m]:
13                    r = m - 1
14                else:
15                    l = m + 1
16            else:
17                # Right half must be sorted
18                # Target is in the sorted right half
19                if nums[m] < target <= nums[r]:
20                    l = m + 1
21                else:
22                    r = m - 1
23
24        return -1
25
26# Time Complexity: O(log n)
27# - Modified binary search that eliminates half the search space each iteration
28# - Even with rotation, we can always identify a sorted half to make decisions
29
30# Space Complexity: O(1)
31# - Only uses constant extra space for pointers (l, r, m)
32# - No recursion or additional data structures that scale with input size