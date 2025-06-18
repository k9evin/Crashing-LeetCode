/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    let prev = null;
    let curr = head;

    while (curr) {
        // Keep a copy of the next node
        let nxt = curr.next;
        // Reverse the current node
        curr.next = prev;
        // Update prev and curr
        prev = curr;
        curr = nxt;
    }

    return prev;
};