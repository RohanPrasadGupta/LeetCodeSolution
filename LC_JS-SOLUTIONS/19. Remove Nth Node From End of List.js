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
  let dummy = new ListNode();
  dummy.next = head;
  let cur = dummy; // Left Pointer from the new dummy node
  let right = head; // To be shifted

  while (n > 0) {
    right = right.next;
    n -= 1;
  }

  while (right) {
    cur = cur.next;
    right = right.next;
  }

  cur.next = cur.next.next;

  return dummy.next;
};
