# Last updated: 1/4/2026, 5:09:01 PM
1class Solution:
2    def lowerBound(self, nums: List[int], target: int) -> int:
3        # Find first index where nums[i] >= target using open interval (l, r)
4        l, r = -1, len(nums)
5        while l + 1 < r:  # While interval (l, r) contains at least one element
6            m = (l + r) // 2
7            if nums[m] < target:
8                l = m  # Search right half (m, r)
9            else:
10                r = m  # Search left half (l, m), m is a candidate
11        return r  # First index >= target
12
13    def successfulPairs(
14        self, spells: List[int], potions: List[int], success: int
15    ) -> List[int]:
16        # Sort potions to enable binary search
17        potions.sort()
18        res = []
19
20        for spell in spells:
21            # Calculate minimum potion strength needed: ceil(success / spell)
22            # Using integer ceiling division: (success + spell - 1) // spell
23            min_potion = (success + spell - 1) // spell
24
25            # Find first potion index that meets the requirement
26            index = self.lowerBound(potions, min_potion)
27
28            # Count of successful potions = total potions - first valid index
29            res.append(len(potions) - index)
30
31        return res
32
33
34# Time Complexity: O(m log m + n log m)
35#   - m log m for sorting potions
36#   - n log m for binary searches (one per spell)
37# Space Complexity: O(1) excluding output array
38