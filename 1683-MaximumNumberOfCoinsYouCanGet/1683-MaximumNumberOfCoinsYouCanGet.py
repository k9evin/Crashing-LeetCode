# Last updated: 12/29/2025, 1:41:27 AM
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        res = 0
        piles.sort()

        for i in range(len(piles) // 3, len(piles), 2):
            res += piles[i]
        return res