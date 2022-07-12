class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Solution 1:
        # Time complexity: O(n)
        # Space complexity: O(1)
        l, r, ans = 0, 1, 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                ans = max(profit, ans)
            # if prices[r] < prices[l] we should buy 
            # stock on the lowest day
            else:
                l = r
            r += 1
        return ans