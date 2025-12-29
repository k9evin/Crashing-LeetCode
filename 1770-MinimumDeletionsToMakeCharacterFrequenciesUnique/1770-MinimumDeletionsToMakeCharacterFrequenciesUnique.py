# Last updated: 12/29/2025, 1:41:14 AM
class Solution:
    def minDeletions(self, s: str) -> int:
        # use defaultdict to prevent does not contain key
        freq = defaultdict(int)
        # count the frequency of a character
        for c in s:
            freq[c] += 1

        res = 0
        visited = set()

        for f in freq.values():
            # decrement the frequency if it's in visited set or > 0
            while f in visited and f > 0:
                f -= 1
                res += 1
            # add the new frequency to the visited set
            visited.add(f)

        return res