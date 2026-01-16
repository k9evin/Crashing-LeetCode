# Last updated: 1/16/2026, 3:36:12 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7# Define less-than operator for ListNode to enable heap comparison
8# This allows Python's heapq to compare ListNode objects directly
9ListNode.__lt__ = lambda a, b: a.val < b.val
10
11
12class Solution:
13    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
14        # Create a dummy node to simplify edge cases
15        dummy = ListNode()
16        curr = dummy  # Pointer to build the merged list
17
18        # Initialize heap with non-empty lists only
19        heap = [lst for lst in lists if lst]
20
21        # Convert list to a min-heap in O(k) time
22        heapify(heap)
23
24        # Process until heap is empty
25        while heap:
26            # Pop the smallest node from the heap
27            node = heappop(heap)
28
29            # Append the node to the merged list
30            curr.next = node
31            curr = node  # Move current pointer forward
32
33            # The next node could also be a smallest node
34            if node.next:
35                heappush(heap, node.next)
36
37        # Return the merged list (skip the dummy node)
38        return dummy.next
39
40
41# Time Complexity: O(N log k)
42# - N = total number of nodes across all lists
43# - Each node is pushed and popped from the heap once: O(N log k)
44# - Heap operations (push/pop) take O(log k) time where k is number of lists
45# - Initial heapify takes O(k) time
46
47# Space Complexity: O(k)
48# - Heap stores at most k nodes (one from each list)
49# - O(1) extra space for pointers (dummy, curr)
50# - Output list uses O(N) space but that's required for the result
51