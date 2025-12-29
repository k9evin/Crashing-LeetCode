# Last updated: 12/29/2025, 1:40:26 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        next_node = self.removeNodes(head.next)

        if next_node and next_node.val > head.val:
            return next_node

        head.next = next_node

        return head