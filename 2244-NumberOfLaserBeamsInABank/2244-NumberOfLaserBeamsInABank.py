# Last updated: 12/29/2025, 1:40:41 AM
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans, temp = 0, 0
        for s in bank:
            n = s.count('1')
            if n == 0:
                continue
            ans += temp * n
            temp = n
        return ans