/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function (head, n) {
    // Handle edge case where head node needs to be removed
    let dummy = new ListNode(0, head);
    let slow = dummy;
    let fast = dummy;

    // Move fast to n steps ahead
    for (let i = 0; i < n; i++) {
        fast = fast.next;
    }

    // Move both pointers until fast reach the end
    while (fast.next !== null) {
        slow = slow.next;
        fast = fast.next;
    }
    // Remove nth node
    slow.next = slow.next.next;

    return dummy.next;
};