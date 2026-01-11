# Last updated: 1/10/2026, 11:53:06 PM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        # Initialize pointers for binary search (closed interval [l, r])
4        l, r = 0, len(nums) - 1
5
6        # Optimization: if array is not rotated (or has only one element),
7        # the first element is the minimum
8        if nums[0] <= nums[-1]:
9            return nums[0]
10
11        # Binary search to find the rotation pivot (minimum element)
12        while l < r:
13            m = l + (r - l) // 2  # Prevents potential overflow
14            
15            # If mid element is greater than rightmost element,
16            # the minimum must be in the right half (after mid)
17            if nums[m] > nums[r]:
18                l = m + 1
19            # Otherwise, the minimum is in the left half (including mid)
20            else:
21                r = m
22
23        # When loop ends, l == r and points to the minimum element
24        return nums[l]