# Last updated: 12/29/2025, 1:40:39 AM
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                num = matrix[i][j]
                if num in rows[i] or num in cols[j]:
                    return False
                rows[i].add(num)
                cols[j].add(num)

        return True
