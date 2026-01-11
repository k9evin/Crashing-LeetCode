# Last updated: 1/11/2026, 12:15:09 AM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        # Initialize binary search pointers (closed interval [l, r])
4        l, r = 0, len(nums) - 1
5
6        while l <= r:
7            m = l + (r - l) // 2  # Middle index (avoids overflow)
8
9            # Found target
10            if nums[m] == target:
11                return m
12
13            # Check if left half [l, m] is sorted (no rotation point)
14            if nums[l] <= nums[m]:
15                # Target is in the sorted left half
16                if nums[l] <= target < nums[m]:
17                    r = m - 1
18                # Target is in the right half (which contains rotation point)
19                else:
20                    l = m + 1
21
22            # Right half [m, r] must be sorted (since left isn't)
23            else:
24                # Target is in the sorted right half
25                if nums[m] < target <= nums[r]:
26                    l = m + 1
27                # Target is in the left half (which contains rotation point)
28                else:
29                    r = m - 1
30
31        return -1  # Target not found
32
33
34# Time Complexity: O(log n) - Binary search halves the search space each iteration
35# Space Complexity: O(1) - Only using constant extra space for pointers
36