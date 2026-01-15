# Last updated: 1/15/2026, 12:29:12 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reorderList(self, head: Optional[ListNode]) -> None:
8        """
9        Do not return anything, modify head in-place instead.
10        """
11        slow = fast = head
12
13        while fast and fast.next:
14            slow = slow.next
15            fast = fast.next.next
16
17        prev, curr = None, slow.next
18        while curr:
19            temp = curr.next
20            curr.next = prev
21            prev = curr
22            curr = temp
23        slow.next = None
24
25        p1, p2 = head, prev
26        while p2:
27            next1 = p1.next
28            next2 = p2.next
29
30            p1.next = p2
31            p1 = next1
32
33            p2.next = p1
34            p2 = next2
35