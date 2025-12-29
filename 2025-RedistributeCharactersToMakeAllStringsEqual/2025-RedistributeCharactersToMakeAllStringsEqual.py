# Last updated: 12/29/2025, 1:40:53 AM
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = collections.defaultdict(int)
        
        for word in words:
            for c in word:
                count[c] += 1

        n = len(words)
        for v in count.values():
            if v % n != 0:
                return False

        return True
