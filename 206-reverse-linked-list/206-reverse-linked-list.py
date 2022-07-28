# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Solution 1: iteratively
        # Time complexity: O(n)
        # Space complexity: O(1)
        # prev, curr = None, head
        # while curr:
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt
        # return prev
		
		# Solution 2: recursively
        # Time complexity: O()
        # Space complexity: O()
        # base case
        if not head or not head.next:
            return head
        newHead = self.reverseList(head.next)
        # connect with its prev element
        head.next.next = head
        head.next = None
        return newHead