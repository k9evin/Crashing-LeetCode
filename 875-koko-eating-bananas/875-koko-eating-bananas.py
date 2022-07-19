class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Solution 1:
        # Time complexity: O(max(p) * logp)
        # Space complexity: O(1)
        
        # piles = [3,6,7,11], h = 8
        # possible solution = [1,2,...,10,11]
        l = 1
        r = max(piles)
        k = 0
        while l <= r:
            m = (l + r) // 2
            totalH = 0
            for p in piles:
                # equivalent to math.ceil(p // m) and ((p - 1) // m) + 1
                totalH += -(p // -m)
            # 如果总时间比h短，那么猴子可以吃慢点
            if totalH <= h:
                k = m
                r = m - 1
            # 如果时间长，那猴子要吃快点
            else:
                l = m + 1

        return k
                