# Last updated: 12/29/2025, 1:41:18 AM
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        last_occurrence = {}
        max_length = -1

        for i, char in enumerate(s):
            if char in last_occurrence:
                max_length = max(max_length, i - last_occurrence[char] - 1)
            else:
                last_occurrence[char] = i

        return max_length