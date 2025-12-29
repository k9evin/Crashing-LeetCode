# Last updated: 12/29/2025, 1:40:40 AM
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        cache = [[-1] * 3 for i in range(len(corridor))]

        def dfs(i, seats):
            if i == len(corridor):
                return 1 if seats == 2 else 0
            
            if cache[i][seats] != -1:
                return cache[i][seats]
            
            res = 0
            if seats == 2:
                if corridor[i] == 'S':
                    res = dfs(i + 1, 1)
                else:
                    res = dfs(i + 1, 0) + dfs(i + 1, 2)
            else:
                if corridor[i] == 'S':
                    res = dfs(i + 1, seats + 1)
                else:
                    res = dfs(i + 1, seats)

            cache[i][seats] = res % MOD

            return res % MOD

        return dfs(0, 0)