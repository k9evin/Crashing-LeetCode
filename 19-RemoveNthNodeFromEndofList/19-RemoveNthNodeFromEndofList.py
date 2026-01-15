# Last updated: 1/15/2026, 1:01:11 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
8        # Step 1: Create a dummy node to handle edge case (removing head)
9        dummy = ListNode(0, head)
10        slow = fast = dummy
11
12        # Step 2: Move fast pointer n+1 steps ahead
13        # This creates a gap of n nodes between fast and slow
14        for _ in range(n + 1):
15            fast = fast.next
16
17        # Step 3: Move both pointers until fast reaches the end
18        # When fast is None, slow will be right before the node to remove
19        while fast:
20            slow = slow.next
21            fast = fast.next
22
23        # Step 4: Remove the nth node from end
24        # slow.next is the node to be removed
25        slow.next = slow.next.next
26
27        # Step 5: Return the new head (dummy.next handles case where head was removed)
28        return dummy.next
29
30
31# Time Complexity: O(L) where L is the length of the linked list
32# - We traverse the list at most once with the fast pointer
33# - The slow pointer follows behind, so total is one pass through the list
34
35# Space Complexity: O(1)
36# - Only uses constant extra space (dummy, slow, fast pointers)
37# - No additional data structures that grow with input size
38