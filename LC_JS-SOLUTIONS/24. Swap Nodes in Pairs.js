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
var swapPairs = function(head) {
    const dummy =new ListNode(0);
    dummy.next = head;
    let prev = dummy;

    while(head && head.next){
        let FirstNode = head
        let SecondNode = head.next

        FirstNode.next =SecondNode.next
        SecondNode.next = FirstNode
        prev.next = SecondNode

        prev = FirstNode
        head =  FirstNode.next
    }
    return dummy.next



};