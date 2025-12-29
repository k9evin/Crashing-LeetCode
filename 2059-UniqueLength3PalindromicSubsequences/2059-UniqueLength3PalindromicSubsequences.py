# Last updated: 12/29/2025, 1:40:47 AM
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0

        # only iterate the unique characters
        for c in set(s):
            # find the first and last occurance of the character
            l_idx, r_idx = s.index(c), s.rindex(c)

            # all the possible middle characters without duplicate
            possible_mid = set(s[l_idx + 1: r_idx])

            # the length of the possible_mid set indicates the possible combinations
            res += len(possible_mid)

        return res
