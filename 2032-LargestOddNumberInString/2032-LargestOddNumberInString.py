# Last updated: 12/29/2025, 1:40:51 AM
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[:i + 1]
            
        return ""