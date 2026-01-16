# Last updated: 1/16/2026, 3:31:00 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7ListNode.__lt__ = lambda a, b: a.val < b.val
8
9
10class Solution:
11    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
12        dummy = ListNode()
13        curr = dummy
14
15        heap = [list for list in lists if list]
16
17        heapify(heap)
18
19        while heap:
20            node = heappop(heap)
21            curr.next = node
22            curr = node
23
24            if node.next:
25                heappush(heap, node.next)
26
27        return dummy.next
28