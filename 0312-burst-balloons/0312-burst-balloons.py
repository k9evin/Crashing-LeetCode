class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        points = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        
        for i in range(n + 1, -1, -1):
            for j in range(i + 1, n + 2):
                for k in range(i + 1, j):
                    
                    dp[i][j] = max(dp[i][j], 
                                   dp[i][k] + dp[k][j] + 
                                   points[i] * points[k] * points[j])

        return dp[0][n + 1]