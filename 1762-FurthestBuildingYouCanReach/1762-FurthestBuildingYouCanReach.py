# Last updated: 12/29/2025, 1:41:15 AM
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        n = len(heights)
        for i in range(n - 1):
            difference = heights[i + 1] - heights[i]
            if difference <= 0:
                continue

            # if climb > 0 (can be omitted)
            heapq.heappush(heap, difference)
            if len(heap) > ladders:
                bricks_needed = heapq.heappop(heap)
                bricks -= bricks_needed
            
            # if we run out of bricks
            if bricks < 0:
                return i
        return n - 1