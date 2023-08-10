class MedianFinder:

    def __init__(self):
        # use a max heap to store the first half of the list
        self.maxHeap = []
        # use a min heap to store the second half of the list
        self.minHeap = []


    def addNum(self, num: int) -> None:
        # always add num to the maxHeap
        heapq.heappush(self.maxHeap, -num)
        # then move the largest num from maxHeap to minHeap, to
        # ensure that maxHeap's elements always smaller than elements
        # in minHeap
        heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        # balance two heaps
        if len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        

    def findMedian(self) -> float:
        # since we ensure that the length of maxHeap is always
        # greater or equal to minHeap, we only need to handle 2 cases
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        else:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()