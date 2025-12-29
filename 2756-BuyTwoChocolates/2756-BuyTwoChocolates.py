# Last updated: 12/29/2025, 1:40:19 AM
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1 = min2 = float('inf')

        for p in prices:
            if p < min1:
                min2, min1 = min1, p
            else:
                min2 = min(min2, p)
        
        leftover = money - (min1 + min2)

        return leftover if leftover >= 0 else money