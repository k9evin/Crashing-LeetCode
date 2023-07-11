# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse the second half of the list
        prev, curr = None, slow.next
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        slow.next = None
        
        # merge two list
        p1, p2 = head, prev
        while p2:
            next1 = p1.next
            next2 = p2.next

            p1.next = p2
            p1 = next1

            p2.next = p1
            p2 = next2

