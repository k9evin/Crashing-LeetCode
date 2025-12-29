# Last updated: 12/29/2025, 1:41:17 AM
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])

        minHeap = [[0, 0, 0]] # [diff, r, c]
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)

            if (r, c) in visited:
                continue
            visited.add((r, c))

            if (r, c) == (m - 1, n - 1):
                return diff

            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if (newR < 0 or newC < 0 or 
                    newR >= m or newC >= n or 
                    (newR, newC) in visited):
                    continue
                newDiff = max(abs(heights[r][c] - heights[newR][newC]), diff)
                heapq.heappush(minHeap, [newDiff, newR, newC])