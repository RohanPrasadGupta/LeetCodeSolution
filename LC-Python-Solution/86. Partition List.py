# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        lessList = lessPointer =  ListNode()
        grtList = grtPointer =  ListNode()


        while(head):
            if head.val < x:
                lessPointer.next = head
                lessPointer = lessPointer.next
            else:
                grtPointer.next = head
                grtPointer = grtPointer.next
            head = head.next
        
        grtPointer.next = None
        lessPointer.next = grtList.next

        return lessList.next
        