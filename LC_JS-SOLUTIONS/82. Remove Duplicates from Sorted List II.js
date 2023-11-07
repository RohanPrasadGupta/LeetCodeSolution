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
var deleteDuplicates = function(head) {

    let dummy = new ListNode(0)
    dummy.next = head
    let prev = dummy
    let current = head

    while (current){
        let isDuplicate = false
        while(current.next && current.val== current.next.val){
            current =  current.next
            isDuplicate = true
        }

        if (isDuplicate==true){
            prev.next = current.next
        }
        else{
            prev = prev.next
        }

        current = current.next

    }

    return dummy.next


    
    
};