# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while(head and head.next):
            FirstNode = head
            SecondNode = head.next

            #SWAPING TWO ADJACENT NODES

            FirstNode.next = SecondNode.next
            SecondNode.next = FirstNode
            prev.next = SecondNode

            #Moving to other Two Node

            prev = FirstNode
            head = FirstNode.next
        
        return dummy.next






