# Last updated: 12/29/2025, 1:40:15 AM
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        
        @cache
        def dp(i, remain):
            # we have painted all the walls
            if remain <= 0:
                return 0
            # we have run out of walls, so it's impossible to paint
            if i == n:
                return inf

            # option 1: paint the ith wall, thus the cost will be
            paint = dp(i + 1, remain - 1 - time[i]) + cost[i]
            # option 2: don't paint the ith wall, we will have the same remaining walls
            nopaint = dp(i + 1, remain)

            return min(paint, nopaint)


        n = len(cost)
        return dp(0, n)
