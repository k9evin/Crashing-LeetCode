# Last updated: 12/29/2025, 1:40:59 AM
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # Check if all bags can have <= max_balls_in_bag with given operations
        def can_divide(max_balls_in_bag):
            total_ops = 0
            for n in nums:
                # Calculate required operations for current bag
                total_ops += ceil(n / max_balls_in_bag) - 1
                if total_ops > maxOperations:
                    return False
            return True

        # Binary search for the minimum possible max balls per bag
        l, r = 1, max(nums)
        while l < r:
            m = (l + r) // 2
            if can_divide(m):
                r = m  # Try for a smaller maximum
            else:
                l = m + 1  # Increase the allowed maximum
        return l  # Minimum possible maximum balls per bag
