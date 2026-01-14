# Last updated: 1/14/2026, 2:02:52 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7
8class Solution:
9    def hasCycle(self, head: Optional[ListNode]) -> bool:
10        # 快慢指针，都从头节点开始
11        fast, slow = head, head
12
13        # 快指针每次走2步，慢指针每次走1步
14        while fast and fast.next:
15            slow = slow.next
16            fast = fast.next.next
17
18            # 如果有环，快指针最终会追上慢指针
19            if slow == fast:
20                return True
21
22        # 快指针到达链表末尾，说明无环
23        return False
24
25
26# Time Complexity: O(N) - N为链表长度，最坏情况遍历整个链表
27# Space Complexity: O(1) - 只使用两个指针变量
28