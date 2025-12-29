# Last updated: 12/29/2025, 1:40:30 AM
class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:


        def dp(distance, k):
            # return the result in cache if exists
            if (distance, k) in cache:
                return cache[distance, k]
        
            # if we reached the position and used all the steps
            if distance == 0 and k == 0:
                return 1
            # if no step left
            elif k < 0:
                return 0

            # calculate the result for moving left and right
            res = dp(distance - 1, k - 1) + dp(distance + 1, k - 1)
            # store the result in cache
            cache[(distance, k)] = res % MOD

            return cache[(distance, k)]


        MOD = 10**9+7
        # cache the (distance, k) result in a dictionary
        cache = {}
        
        return dp(abs(endPos - startPos), k)