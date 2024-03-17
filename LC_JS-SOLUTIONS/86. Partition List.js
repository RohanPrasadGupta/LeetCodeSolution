/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} x
 * @return {ListNode}
 */
var partition = function (head, x) {
  let lessList = new ListNode();
  let lessPointer = lessList;

  let grtList = new ListNode();
  let grtPointer = grtList;

  while (head) {
    if (head.val < x) {
      lessPointer.next = head;
      lessPointer = lessPointer.next;
    } else {
      grtPointer.next = head;
      grtPointer = grtPointer.next;
    }
    head = head.next;
  }

  grtPointer.next = null;
  lessPointer.next = grtList.next;

  return lessList.next;
};
