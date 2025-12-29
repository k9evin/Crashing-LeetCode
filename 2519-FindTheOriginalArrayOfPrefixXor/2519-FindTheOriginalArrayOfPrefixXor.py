# Last updated: 12/29/2025, 1:40:28 AM
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        for i in range(len(pref) - 1, 0, -1):
            pref[i] ^= pref[i - 1]
        return pref