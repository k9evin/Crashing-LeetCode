# Last updated: 12/29/2025, 1:40:45 AM
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        countA, countB = 0, 0
        for i in range(1, len(colors) - 1):
            if colors[i - 1] == colors[i] == colors[i + 1]:
                if colors[i] == 'A':
                    countA += 1
                if colors[i] == 'B':
                    countB += 1

        return countA > countB