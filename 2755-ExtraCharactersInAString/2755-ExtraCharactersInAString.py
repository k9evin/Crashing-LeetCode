# Last updated: 12/29/2025, 1:40:20 AM
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = [0] * (len(s) + 1)

        # "leetscode"
        # ["leet","code","leetcode"]
        # [0, 1, 2, 3, 0, 1, 2, 3, 4, 1]
        # dp[i]代表s[0...i]有多少个多余字符
        for i in range(1, len(s) + 1):
            dp[i] = dp[i - 1] + 1
            
            for w in dictionary:
                # 如果s[i - len(w): i]和w相同，那么s[i-len(w):i]可以组成单词，更新dp[i] = min(dp[i], dp[i - len(w)])
                if s[i - len(w): i] == w:
                    dp[i] = min(dp[i], dp[i - len(w)])
        return dp[-1]
