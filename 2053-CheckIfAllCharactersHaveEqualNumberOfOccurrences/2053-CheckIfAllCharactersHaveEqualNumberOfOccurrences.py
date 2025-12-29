# Last updated: 12/29/2025, 1:40:48 AM
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        s_count = Counter(s)
        return len(set(s_count.values())) == 1
