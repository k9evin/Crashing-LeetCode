# Last updated: 12/29/2025, 1:40:35 AM
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ''

        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                res = max(res, num[i])

        return res * 3

        