/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var swapNodes = function (head, k) {
  let cur = head;
  for (let i = 0; i < k - 1; i++) {
    cur = cur.next;
  }

  let left = cur;
  let right = head;
  while (cur.next) {
    cur = cur.next;
    right = right.next;
  }

  let temp = left.val;
  left.val = right.val;
  right.val = temp;

  return head;
};
