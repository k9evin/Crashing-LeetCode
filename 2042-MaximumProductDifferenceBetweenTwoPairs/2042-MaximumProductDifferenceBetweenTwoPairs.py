# Last updated: 12/29/2025, 1:40:50 AM
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max1 = max2 = 0
        min1 = min2 = float('inf')

        for n in nums:
            if n > max1:
                max2 = max1
                max1 = n
            else:
                max2 = max(n, max2)
            if n < min1:
                min2 = min1
                min1 = n
            else:
                min2 = min(n, min2)

        return (max1 * max2) - (min1 * min2)