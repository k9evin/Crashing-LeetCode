class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-1 * i for i in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            y = -1 * heapq.heappop(heap)
            x = -1 * heapq.heappop(heap)
            if x != y:
                res = -1 * (y - x)
                heapq.heappush(heap, res)
        return -1 * heap[0] if len(heap) > 0 else 0