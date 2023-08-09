class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # use minHeap
        self.heap = nums
        self.k = k
        # transfer list into a heap
        heapq.heapify(self.heap)
        # maintain size k
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # add value if the size of the heap is smaller than k
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        # add the value then pop the smallest value from the heap
        else:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)