# Last updated: 12/29/2025, 1:40:24 AM
class Solution:
    def findScore(self, nums: List[int]) -> int:
        # Initialize a min heap to store (num, i) tuples
        heap = [(n, i) for i, n in enumerate(nums)]
        heapq.heapify(heap)
        # Initialize a set to track the marked index
        marked_index = set()
        score = 0

        while heap:
            # Retrieve the smallest num from heap
            n, i = heapq.heappop(heap)
            # If the current index has not been marked, add
            # the num to score and mark its adjacent elements
            if i not in marked_index:
                score += n
                marked_index.add(i - 1)
                marked_index.add(i)
                marked_index.add(i + 1)

        return score
