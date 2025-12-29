# Last updated: 12/29/2025, 1:41:18 AM
class Solution:
    def maxDepth(self, s: str) -> int:
        max_nested = 0
        curr_nested = 0

        for c in s:
            if c == "(":
                curr_nested += 1
            elif c == ")":
                max_nested = max(max_nested, curr_nested)
                curr_nested -= 1

        return max_nested
